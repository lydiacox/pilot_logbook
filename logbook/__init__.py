import os
from flask import Flask, json, jsonify, request
from flask_sqlalchemy import SQLAlchemy

(
    db_user,
    db_pass,
    db_name,
    db_domain
) = (os.environ.get(item) for item in [
    "DB_USER",
    "DB_PASS",
    "DB_NAME",
    "DB_DOMAIN"
    ]
)

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql+psycopg2://{db_user}:{db_pass}@{db_domain}/{db_name}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

db = SQLAlchemy(app)

print(db)

class Pilot(db.Model):
    __tablename__ = "pilots"
    pilot_id = db.Column(db.Integer, primary_key=True)
    pilot_name = db.Column(db.String(100), nullable=False)

    def __init__(self, pilot_id):
        self.pilot_id = pilot_id

    @property
    def serialize(self):
        return {
            "pilot_id": self.pilot_id,
            "pilot_name": self.pilot_name
        }

db.create_all()

@app.route('/')
def home_page():
    """
    The homepage route.
    """
    return 'Hello, world! Welcome to Pilot Logbook!'

@app.route('/pilots/', methods=["GET"])
def get_pilots():
    pilots = Pilot.query.all()
    return jsonify([pilot.serialize for pilot in pilots])

@app.route("/pilots/new/", methods=["POST"])
def create_pilot():
    new_pilot=Pilot(request.json['pilot_name'])
    db.session.add(new_pilot)
    db.session.commit()
    return jsonify(new_pilot.serialize)

@app.route("/pilots/<int:id>", methods=["GET"])
def get_pilot(id):
    pilot = Pilot.query.get_or_404(id)
    return jsonify(pilot.serialize)

@app.route("/pilots/<int:id>", methods=["PUT", "PATCH"])
def update_pilot(id):
    pilot = Pilot.query.filter_by(pilot_id=id)
    pilot.update(dict(pilot_name=request.json["pilot_name"]))
    db.session.commit()
    return jsonify(pilot.first().serialize)

@app.route("/pilots/<int:id>/", methods=["DELETE"])
def delete_pilot(id):
    pilot = Pilot.query.get_or_404(id)
    db.session.delete(pilot)
    db.session.commit()
    return jsonify(pilot.serialize)

if __name__ == '__main__':
    pass

@app.route('/pilots/<int:pilot_id>/')
def get_specific_pilots(pilot_id):
    return f'This will be a page displaying information about pilot {pilot_id}.'

@app.route('/calc/<int:f_num>/<string:operator>/<int:s_num>')
def calculate(f_num, operator, s_num):
    if operator in ['+', '-', '*', '/']:
        return f"{eval(f'{f_num}{operator}{s_num}')}"
    return "Please enter a valid calculation"

if __name__ == '__main__':
    app.run(debug=True)
    