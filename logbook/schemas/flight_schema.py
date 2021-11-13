from enum import auto

from marshmallow import validate
from logbook.schemas.flight_schema import FlightSchema
from main import ma
from models.flights import Flight
from marshmallow_sqlalchemy import auto_field
from marshmallow.validate import Length

class FlightSchema(ma.SQLAlchemyAutoSchema):
    flight_id = auto_field(dump_only=True)
    flight_no = auto_field(required=True, validate=Length(min=1, max=10))

    class Meta:
        model = Flight
        load_instance = True

flight_schema = FlightSchema()
multi_flight_schema = FlightSchema(many=True)