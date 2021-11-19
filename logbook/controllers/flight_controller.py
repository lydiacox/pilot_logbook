from flask import Blueprint, jsonify, request, render_template, redirect, url_for, current_app
from main import db
from models.flights import Flight
from schemas.flight_schema import flight_schema, multi_flight_schema
import boto3

flights = Blueprint('flights', __name__)

# The homepage, no CRUD resource
@flights.route('/')
def home_page():
    """
    The homepage route.
    """
    data = {
        "page_title": "Homepage"
    }
    return render_template("homepage.html", page_data=data)

# The GET route endpoint
@flights.route('/flights/', methods=["GET"])
def get_flights():
    data = {
        "page_title": "Flight Index",
        "flights": multi_flight_schema.dump(Flight.query.all())
    }
    return render_template("flight_index.html", page_data=data)

#The POST route endpoint
@flights.route("/flights/", methods=["POST"])
def create_flight():
    print(request.form)
    new_flight=flight_schema.load(request.form)
    db.session.add(new_flight)
    db.session.commit()
    return redirect(url_for("flights.get_flights"))

# An endpoint to get info for a particular flight
@flights.route("/flights/<int:id>/", methods=["GET"])
def get_flight(id):
    flight = Flight.query.get_or_404(id)

    s3_client=boto3.client("s3")
    bucket_name = current_app.config["AWS_S3_BUCKET"]
    image_url = s3_client.generate_presigned_url(
        "get_object",
        Params={
            "Bucket": bucket_name,
            "Key": flight.image_filename
        },
        ExpiresIn=100
    )

    data = {
        "page_title": "Flight Detail",
        "flight": flight_schema.dump(flight),
        "image": image_url
    }
    print(data)
    return render_template("flight_detail.html", page_data=data)

# A POST route to update flight info
@flights.route("/flights/<int:id>/", methods=["POST"])
def update_flight(id):
    flight = Flight.query.filter_by(flight_id=id)
    update_fields = flight_schema.dump(request.form)
    if update_fields:
        flight.update(update_fields)
        db.session.commit()
    data = {
        "page_title": "Flight Detail",
        "flight": flight_schema.dump(flight.first())
    }
    return render_template("flight_detail", page_data=data)

# A DELETE method
@flights.route("/flights/<int:id>/delete/", methods=["POST"])
def delete_flight(id):
    flight = Flight.query.get_or_404(id)
    db.session.delete(flight)
    db.session.commit()
    return redirect(url_for("flights.get_flights"))
