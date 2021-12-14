from main import ma
from models.approach import InstrumentApproach
from marshmallow_sqlalchemy import auto_field

class ApproachSchema(ma.SQLAlchemyAutoSchema):
    """
    A class to represent an instrument approach schema.
    ...
    Attributes
    ----------
    approach_id : int
        the primary key
    approach_type : str
        ILS, RNP, VOR, NDB or Visual
    approach_flight_id : int
        foreign key of the related flight
    approach_flight : dict
        nested FlightSchema
    """

    approach_id = auto_field(dump_only=True)
    approach_type = auto_field(required=True)
    approach_flight_id = auto_field(required=True)

    approach_flight = ma.Nested("FlightSchema")

    class Meta:
        model = InstrumentApproach
        load_instance = True

approach_schema = ApproachSchema()
multi_approach_schema = ApproachSchema(many=True)