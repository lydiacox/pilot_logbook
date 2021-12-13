from sqlalchemy.orm import relationship
from main import db

# Tells the ORM what tables should exist in the database
# Allows us to retrieve info from those tables
class Flight(db.Model):
    """
    A class to represent a flight model.
    ...
    Attributes
    ----------
    flight_id : int
        the primary key
    date_began : date
        the date the flight started
    take_off_landing_points : string
        IATA codes for all take off and landing points
    pilot_in_command : string
        the name of the pilot in command
    other_crew : string
        the name(s) of any other flight crew
    single_engine_icus_day : float between 0 and 24
        day hours in single engine aircraft in command under supervision
    single_engine_icus_night : float between 0 and 24
        night hours in single engine aircraft in command under supervision
    single_engine_dual_day : float between 0 and 24
        day hours second in command in single engine aircraft
    single_engine_dual_night : float between 0 and 24
        night hours second in command in single engine aircraft
    single_engine_command_day : float between 0 and 24
        day hours in command of single engine aircraft
    single_engine_command_night : float between 0 and 24
        night hours in command of single engine aircraft
    multi_engine_icus_day : float between 0 and 24
        day hours in multi engine aircraft in command under supervision
    multi_engine_icus_night : float between 0 and 24
        night hours in multi engine aircraft in command under supervision
    multi_engine_dual_day : float between 0 and 24
        day hours second in command in multi engine aircraft
    multi_engine_dual_night : float between 0 and 24
        night hours second in command in multi engine aircraft
    multi_engine_command_day : float between 0 and 24
        day hours in command of multi engine aircraft
    multi_engine_command_night : float between 0 and 24
        night hours in command of multi engine aircraft
    multi_engine_co_pilot_day : float between 0 and 24
        day hours co-piloting in multi engine aircraft
    multi_engine_co_pilot_night : float between 0 and 24
        night hours co-piloting in multi engine aircraft
    instrument_in_flight : float between 0 and 24
        XXXXXXXXXXXXX
    instrument_ground : float between 0 and 24
        hours in a flight simulator
    creator : foreign key
        user_id field from the users model
    aircraft : foreign key
        aircraft_id field from the aircraft model
    """
    __tablename__ = "flights"

    flight_id = db.Column(db.Integer, primary_key=True)
    date_began = db.Column(db.String(10), nullable=False, server_default="1/1/1900")
    take_off_landing_points = db.Column(db.String(200), nullable=False)
    pilot_in_command = db.Column(db.String(100), nullable=False)
    other_crew = db.Column(db.String(200))
    single_engine_icus_day = db.Column(db.Float(precision=1))
    single_engine_icus_night = db.Column(db.Float(precision=1))
    single_engine_dual_day = db.Column(db.Float(precision=1))
    single_engine_dual_night = db.Column(db.Float(precision=1))
    single_engine_command_day = db.Column(db.Float(precision=1))
    single_engine_command_night = db.Column(db.Float(precision=1))
    multi_engine_icus_day = db.Column(db.Float(precision=1))
    multi_engine_icus_night = db.Column(db.Float(precision=1))
    multi_engine_dual_day = db.Column(db.Float(precision=1))
    multi_engine_dual_night = db.Column(db.Float(precision=1))
    multi_engine_command_day = db.Column(db.Float(precision=1))
    multi_engine_command_night = db.Column(db.Float(precision=1))
    multi_engine_co_pilot_day = db.Column(db.Float(precision=1))
    multi_engine_co_pilot_night = db.Column(db.Float(precision=1))
    instrument_in_flight = db.Column(db.Float(precision=1))
    instrument_ground = db.Column(db.Float(precision=1))
    # One to many relationship, uni-directional, with users (child)
    creator = db.Column(db.Integer, db.ForeignKey("flasklogin-users.user_id"))
    # Many to one relationship, bi-directional, to aircraft (parent)
    aircraft_child_id = db.Column(db.Integer, db.ForeignKey("aircraft.aircraft_id"))
    aircraft = db.relationship("Aircraft", back_populates="flight_no", lazy="joined")
    # One to many relationship to instrument_approach


    # @property
    # Write decorators that add up the columns above into sensible groups
