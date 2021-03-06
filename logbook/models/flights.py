from sqlalchemy.orm import relationship
from main import db
from models.users import User
from models.aircraft import Aircraft
from models.approach import InstrumentApproach

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
    take_off_landing_points : str
        IATA codes for all take off and landing points
    pilot_in_command : str
        the name of the pilot in command
    other_crew : str
        the name(s) of any other flight crew
    single_engine_icus_day : float
        day hours in single engine aircraft in command under supervision
    single_engine_icus_night : float
        night hours in single engine aircraft in command under supervision
    single_engine_dual_day : float
        day hours second in command in single engine aircraft
    single_engine_dual_night : float
        night hours second in command in single engine aircraft
    single_engine_command_day : float
        day hours in command of single engine aircraft
    single_engine_command_night : float
        night hours in command of single engine aircraft
    multi_engine_icus_day : float
        day hours in multi engine aircraft in command under supervision
    multi_engine_icus_night : float
        night hours in multi engine aircraft in command under supervision
    multi_engine_dual_day : float
        day hours second in command in multi engine aircraft
    multi_engine_dual_night : float
        night hours second in command in multi engine aircraft
    multi_engine_command_day : float
        day hours in command of multi engine aircraft
    multi_engine_command_night : float
        night hours in command of multi engine aircraft
    multi_engine_co_pilot_day : float
        day hours co-piloting in multi engine aircraft
    multi_engine_co_pilot_night : float
        night hours co-piloting in multi engine aircraft
    instrument_in_flight : float
        instrument hours in flight
    instrument_ground : float
        hours in a flight simulator
    creator_id : int
        foreign key of the user
    creator : 
        1:M relationship with the user
    aircraft_flight_id : int
        foreign key of the aircraft
    aircraft : 
        1:M relationship with the aircraft
    approach : list
        1:M relationship with the approaches
    """
    __tablename__ = "flights"

    flight_id = db.Column(db.Integer, primary_key=True)
    date_began = db.Column(db.DateTime, nullable=False, server_default="1/1/1900")
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
    # One to many relationship, bi-directional, with users (child)
    creator_id = db.Column(db.Integer, db.ForeignKey("flasklogin-users.user_id"))
    creator = db.relationship("User", back_populates="flights", lazy="joined")
    # One to many relationship, bi-directional, to aircraft (child)
    aircraft_flight_id = db.Column(db.Integer, db.ForeignKey("aircraft.aircraft_id"))
    aircraft = db.relationship("Aircraft", back_populates="flight_no", lazy="joined")
    # One to many relationship, bi-directional, to instrument_approach (parent)
    approach = db.relationship("InstrumentApproach", back_populates="approach_flight", lazy="joined")

    # @property
    # Write decorators that add up the columns above into sensible groups
