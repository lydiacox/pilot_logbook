import os
from flask import Flask, jsonify, request
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

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgres+psycopg2://{db_user}:{db_pass}@{db_domain}/{db_name}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

db = SQLAlchemy(app)

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

@app.route('/')
def hello_world():
    return 'Hello, world!'

@app.route('/pilots/')
def get_pilots():
    return 'This will be a list of all the pilots.'

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