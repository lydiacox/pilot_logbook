from main import ma
from models.flights import Flight
from marshmallow_sqlalchemy import auto_field
from marshmallow.validate import Length, Range

class FlightSchema(ma.SQLAlchemyAutoSchema):
    flight_id = auto_field(dump_only=True)
    aircraft_type = auto_field(required=True, validate=Length(min=1))
    aircraft_rego = auto_field(required=True, validate=Length(min=1, max=10))
    flight_date = auto_field(required=True)
    pilot_in_command = auto_field(required=True)
    other_crew = auto_field()
    details = auto_field(required=True)
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

    class Meta:
        model = Flight
        load_instance = True

flight_schema = FlightSchema()
multi_flight_schema = FlightSchema(many=True)