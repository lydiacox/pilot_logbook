from main import ma
from models.aircraft import Aircraft
from marshmallow_sqlalchemy import auto_field

class AircraftSchema(ma.SQLAlchemyAutoSchema):
    """
    A class to represent an aircraft schema.
    ...
    Attributes
    ----------
    aircraft_id : int
        the primary key
    multi_engine : bool
        false for single engine true for multi engine
    type : str
        aircraft make and model
    nationality : str
        country of registration
    registration : str
        registration number
    """

    aircraft_id = auto_field(dump_only=True)
    multi_engine = auto_field(required=True)
    type = auto_field(required=True)
    nationality = auto_field(required=True)
    registration = auto_field(required=True)

    flight_no = ma.Nested("FlightSchema")

    class Meta:
        model = Aircraft
        load_instance = True

aircraft_schema = AircraftSchema()
multi_aircraft_schema = AircraftSchema(many=True)