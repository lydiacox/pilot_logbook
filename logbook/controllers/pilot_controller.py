from flask import Blueprint, jsonify, request, render_template, redirect, url_for
from main import db
from models.pilot import Pilot
from schemas.pilot_schema import pilot_schema, pilots_schema

pilots = Blueprint('pilots', __name__)

# The homepage, no CRUD
@pilots.route('/')
def home_page():
    """
    The homepage route.
    """
    data = {
        "page_title": "Homepage",
    }
    return render_template("homepage.html", page_data=data)

# The GET route endpoint
@pilots.route('/pilots/', methods=["GET"])
def get_pilots():
    data = {
        "page_title": "Pilot Index",
        "pilots": pilots_schema.dump(Pilot.query.all())
    }
    return render_template("pilot_index.html", page_data=data)

# The POST route endpoint
@pilots.route("/pilots/", methods=["POST"])
def create_pilot():
    new_pilot=pilot_schema.load(request.form)
    db.session.add(new_pilot)
    db.session.commit()
    return redirect(url_for("pilots.get_pilots"))

# An endpoint to get info for a particular pilot
@pilots.route("/pilots/<int:id>/", methods=["GET"])
def get_pilot(id):
    pilot = Pilot.query.get_or_404(id)
    data = {
        "page_title": "Pilot Detail",
        "pilot": pilot_schema.dump(pilot)
    }
    return render_template("pilot_detail.html", page_data=data)

# An POST route to update pilot info
@pilots.route("/pilots/<int:id>/", methods=["POST"])
def update_pilot(id):
    pilot = Pilot.query.filter_by(pilot_id=id)
    updated_fields = pilot_schema.dump(request.form)
    if updated_fields:
        pilot.update(updated_fields)
        db.session.commit()
    data = {
        "page_title": "Pilot Detail",
        "pilot": pilot_schema.dump(pilot.first())
    }
    return render_template("pilot_detail.html", page_data=data)

# A DELETE method
@pilots.route("/pilots/<int:id>/", methods=["POST"])
def delete_pilot(id):
    pilot = Pilot.query.get_or_404(id)
    db.session.delete(pilot)
    db.session.commit()
    return redirect(url_for("pilots.get_pilots"))
