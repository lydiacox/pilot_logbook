from main import ma
from models.approach import InstrumentApproach
from marshmallow_sqlalchemy import auto_field

class ApproachSchema(ma.SQLAlchemyAutoSchema):
    """
    A class to represent an instrument approach schema.
    ...
    Attributes
    ----------
    """

ifr_approach_id = auto_field(dump_only=True)
# add more validation??
approach_type = auto_field(required=True)
approach_flight_id = auto_field(required=True)

approach_flight = ma.Nested("FlightSchema")

class Meta:
    model = InstrumentApproach
    load_instance = True

approach_schema = ApproachSchema()
multi_approach_schema = ApproachSchema(many=True)