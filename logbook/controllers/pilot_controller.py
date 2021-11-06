from flask import Blueprint, jsonify, request
from main import db
from models.pilot import Pilot
from schemas.pilot_schema import pilot_schema, pilots_schema

pilots = Blueprint('pilots', __name__)

@pilots.route('/')
def home_page():
    """
    The homepage route.
    """
    return 'Hello, world! Welcome to Pilot Logbook!'

@pilots.route('/pilots/', methods=["GET"])
def get_pilots():
    pilots = Pilot.query.all()
    return jsonify(pilots_schema.dump(pilots))

@pilots.route("/pilots/new/", methods=["POST"])
def create_pilot():
    new_pilot=pilot_schema.load(request.json)
    db.session.add(new_pilot)
    db.session.commit()
    return jsonify(pilot_schema.dump(new_pilot))

@pilots.route("/pilots/<int:id>/", methods=["GET"])
def get_pilot(id):
    pilot = Pilot.query.get_or_404(id)
    return jsonify(pilot_schema.dump(pilot))

@pilots.route("/pilots/<int:id>/", methods=["PUT", "PATCH"])
def update_pilot(id):
    pilot = Pilot.query.filter_by(pilot_id=id)
    updated_fields = pilot_schema.dump(request.json)
    if updated_fields:
        pilot.update(updated_fields)
        db.session.commit()
    return jsonify(pilot_schema.dump(pilot.first()))

@pilots.route("/pilots/<int:id>/", methods=["DELETE"])
def delete_pilot(id):
    pilot = Pilot.query.get_or_404(id)
    db.session.delete(pilot)
    db.session.commit()
    return jsonify(pilot_schema.dump(pilot))
