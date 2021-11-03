from flask import Blueprint, jsonify, request
from main import db
from models.pilot import Pilot

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
    return jsonify([pilot.serialize for pilot in pilots])

@pilots.route("/pilots/new/", methods=["POST"])
def create_pilot():
    new_pilot=Pilot(request.json['pilot_name'])
    db.session.add(new_pilot)
    db.session.commit()
    return jsonify(new_pilot.serialize)

@pilots.route("/pilots/<int:id>", methods=["GET"])
def get_pilot(id):
    pilot = Pilot.query.get_or_404(id)
    return jsonify(pilot.serialize)

@pilots.route("/pilots/<int:id>", methods=["PUT", "PATCH"])
def update_pilot(id):
    pilot = Pilot.query.filter_by(pilot_id=id)
    pilot.update(dict(pilot_name=request.json["pilot_name"]))
    db.session.commit()
    return jsonify(pilot.first().serialize)

@pilots.route("/pilots/<int:id>/", methods=["DELETE"])
def delete_pilot(id):
    pilot = Pilot.query.get_or_404(id)
    db.session.delete(pilot)
    db.session.commit()
    return jsonify(pilot.serialize)

if __name__ == '__main__':
    pass

@pilots.route('/pilots/<int:pilot_id>/')
def get_specific_pilots(pilot_id):
    return f'This will be a page displaying information about pilot {pilot_id}.'

@pilots.route('/calc/<int:f_num>/<string:operator>/<int:s_num>')
def calculate(f_num, operator, s_num):
    if operator in ['+', '-', '*', '/']:
        return f"{eval(f'{f_num}{operator}{s_num}')}"
    return "Please enter a valid calculation"
