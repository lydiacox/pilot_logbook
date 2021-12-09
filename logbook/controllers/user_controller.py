from flask import Blueprint, request, render_template, redirect, url_for, abort, current_app
from main import db, lm
from models.users import User
from models.flights import Flight
from schemas.user_schema import user_schema, multi_user_schema, user_update_schema
from flask_login import login_user, logout_user, login_required, current_user
from marshmallow import ValidationError
import boto3
from sqlalchemy import func

@lm.user_loader
def load_user(user):
    return User.query.get(user)

@lm.unauthorized_handler
# Have to supply when we're setting up an authorisation system
def unauthorised():
    return redirect("/users/login")

users = Blueprint("users", __name__)

@users.route("/users/", methods=["GET"])
def get_users():
    """Displays a list of users from the database"""
    data = {
        "page_title": "User Index",
        "users": multi_user_schema.dump(User.query.all())
    }
    return render_template("user_index.html", page_data=data)

@users.route("/users/signup/", methods=["GET", "POST"])
def sign_up():
    """Displays the signup form and creates a new user when the form is submitted"""
    data = {
        "page_title": "Sign Up to Pilot Logbook"
    }
    if request.method == "GET":
        return render_template("signup.html", page_data=data)
    
    new_user = user_schema.load(request.form)
    db.session.add(new_user)
    db.session.commit()
    login_user(new_user)
    return redirect(url_for("users.get_users"))

@users.route("/users/login/", methods=["GET","POST"])
def log_in():
    data = {"page_title": "Log In"}

    if request.method == "GET":
        return render_template("login.html", page_data = data)

    user = User.query.filter_by(email=request.form["email"]).first()
    if user and user.check_password(password=request.form["password"]):
        login_user(user)
        return redirect(url_for("flights.get_flights"))

    abort(401, "Login unsuccessful. Did you supply the correct username and password?")

@users.route("/users/account/", methods=["GET", "POST"])
# This decorator makes it impossible to access if you're not logged in.
# If you're not logged in, will redirect you to the login page.
@login_required
def user_detail():

    user = User.query.filter_by(id = current_user.id).first()
    print(user)
    s3_client=boto3.client("s3")
    bucket_name=current_app.config["AWS_S3_BUCKET"]
    image_url = s3_client.generate_presigned_url(
        "get_object",
        Params={
            "Bucket": bucket_name,
            "Key": user.image_filename
        },
        ExpiresIn=100
    )
    hours = db.session.query(func.sum(Flight.hours)).filter(User.id==current_user).scalar
    if request.method == "GET":
        data = {"page_title": "Account Details", "image": image_url, "hours": hours}
        return render_template("user_details.html", page_data = data)

    updated_fields = user_schema.dump(request.form)
    # Validation happens when the schema loads, but not schema dumps, so we need to specify
    # that the fields should be validated
    errors = user_update_schema.validate(updated_fields)
    
    if errors:
        raise ValidationError(message = errors)

    user.update(updated_fields)
    db.session.commit()
    return redirect(url_for("users.get_users"))

@users.route("/users/logout/", methods=["POST"])
@login_required
def log_out():
    logout_user()
    return redirect(url_for("users.log_in"))
