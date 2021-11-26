from flask import Blueprint, jsonify, request, render_template, redirect, url_for, current_app, abort
from main import db
from models.flights import Flight
from schemas.flight_schema import flight_schema, multi_flight_schema
from flask_login import login_required, current_user
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
@login_required
def get_flights():
    data = {
        "page_title": "Flight Index",
        "flights": multi_flight_schema.dump(Flight.query.all())
    }
    return render_template("flight_index.html", page_data=data)

#The POST route endpoint
@flights.route("/flights/", methods=["POST"])
@login_required
def create_flight():
    new_flight=flight_schema.load(request.form)
    new_flight.creator = current_user
    db.session.add(new_flight)
    db.session.commit()
    # print(flight_schema.dump(new_flight))
    return redirect(url_for("flights.get_flights"))

# An endpoint to get info for a particular flight
@flights.route("/flights/<int:id>/", methods=["GET"])
@login_required
def get_flight(id):
    flight = Flight.query.get_or_404(id)
    if current_user.id != flight.creator_id:
        abort(403, "You do not have permission to view this flight")
    data = {
        "page_title": "Flight Detail",
        "flight": flight_schema.dump(flight),
    }
    return render_template("flight_detail.html", page_data=data)

# A POST route to update flight info
@flights.route("/flights/<int:id>/", methods=["POST"])
@login_required
def update_flight(id):
    flight = Flight.query.filter_by(flight_id=id)
    if current_user.id != flight.creator_id:
        abort(403, "You do not have permission to view this flight")
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
@login_required
def delete_flight(id):
    flight = Flight.query.get_or_404(id)
    if current_user.id != flight().creator_id:
        abort(403, "You do not have permission to delete this flight")
    db.session.delete(flight)
    db.session.commit()
    return redirect(url_for("flights.get_flights"))
