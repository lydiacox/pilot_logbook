from main import ma
from models.flights import Flight
from marshmallow_sqlalchemy import auto_field
from marshmallow.validate import Length, Range
from datetime import datetime

class FlightSchema(ma.SQLAlchemyAutoSchema):
    """
    A class to represent a flight schema.
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
    single_engine_icus_day : float
        between 0 and 24 day hours in single engine aircraft in command under supervision
    single_engine_icus_night : float
        between 0 and 24 night hours in single engine aircraft in command under supervision
    single_engine_dual_day : float
        between 0 and 24 day hours second in command in single engine aircraft
    single_engine_dual_night : float
        between 0 and 24 night hours second in command in single engine aircraft
    single_engine_command_day : float
        between 0 and 24 day hours in command of single engine aircraft
    single_engine_command_night : float
        between 0 and 24 night hours in command of single engine aircraft
    multi_engine_icus_day : float
        between 0 and 24 day hours in multi engine aircraft in command under supervision
    multi_engine_icus_night : float
        between 0 and 24 night hours in multi engine aircraft in command under supervision
    multi_engine_dual_day : float
        between 0 and 24 day hours second in command in multi engine aircraft
    multi_engine_dual_night : float
        between 0 and 24 night hours second in command in multi engine aircraft
    multi_engine_command_day : float
        between 0 and 24 day hours in command of multi engine aircraft
    multi_engine_command_night : float
        between 0 and 24 night hours in command of multi engine aircraft
    multi_engine_co_pilot_day : float
        between 0 and 24 day hours co-piloting in multi engine aircraft
    multi_engine_co_pilot_night : float
        between 0 and 24 night hours co-piloting in multi engine aircraft
    instrument_in_flight : float
        between 0 and 24 instrument hours in flight
    instrument_ground : float
        between 0 and 24 hours in a flight simulator
    creator_id : int
        user_id field from the users schema
    aircraft_flight_id : int
        aircraft_id from the aircraft schema
    creator : dict
        nested UserSchema
    aircraft : dict
        nested AircraftSchema
    approach : dict
        nested ApproachSchema
    """
    class Meta:
        model = Flight
        load_instance = True
    
    flight_id = auto_field(dump_only=True)
    date_began = auto_field(required=True, validate=lambda x: x < datetime.now())
    take_off_landing_points = auto_field(required=True)
    pilot_in_command = auto_field(required=True)
    other_crew = auto_field(required = False)
    single_engine_icus_day = auto_field(required = False, validate=Range(0, 24))
    single_engine_icus_night = auto_field(required = False, validate=Range(0, 24))
    single_engine_dual_day = auto_field(required = False, validate=Range(0, 24))
    single_engine_dual_night = auto_field(required = False, validate=Range(0, 24))
    single_engine_command_day = auto_field(required = False, validate=Range(0, 24))
    single_engine_command_night = auto_field(required = False, validate=Range(0, 24))
    multi_engine_icus_day = auto_field(required = False, validate=Range(0, 24))
    multi_engine_icus_night = auto_field(required = False, validate=Range(0, 24))
    multi_engine_dual_day = auto_field(required = False, validate=Range(0, 24))
    multi_engine_dual_night = auto_field(required = False, validate=Range(0, 24))
    multi_engine_command_day = auto_field(required = False, validate=Range(0, 24))
    multi_engine_command_night = auto_field(required = False, validate=Range(0, 24))
    multi_engine_co_pilot_day = auto_field(required = False, validate=Range(0, 24))
    multi_engine_co_pilot_night = auto_field(required = False, validate=Range(0, 24))
    instrument_in_flight = auto_field(required = False, validate=Range(0, 24))
    instrument_ground = auto_field(required = False, validate=Range(0, 24))
    creator_id = auto_field(required=False)
    aircraft_flight_id = auto_field(required=False)
    
    # references the relationship between the user and flight models
    creator = ma.Nested("UserSchema")
    aircraft = ma.Nested("AircraftSchema")
    approach = ma.Nested("ApproachSchema")


flight_schema = FlightSchema()
multi_flight_schema = FlightSchema(many=True)