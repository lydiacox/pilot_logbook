from main import ma
from models.pilots import Pilot
from marshmallow_sqlalchemy import auto_field

class PilotSchema(ma.SQLAlchemyAutoSchema):
    """
    A class to represent a pilot schema.
    ...
    Attributes
    ----------
    pilot_id : int
        the primary key
    arn : int
        the pilot's aviation reference number
    licence_class : str
        rpl, ppl, cpl or atpl
    ariel_application_rating : bool
    instructor_rating : str
        grade 1, grade 2 or grade 3
    instrument_rating : bool
    low_level_rating : bool
    night_vfr_rating : bool
    night_visual_imaging_sys_rating : bool
    """

    pilot_id = auto_field(dump_only=True)
    arn = auto_field(required=False)
    # add data validation
    licence_class = auto_field(required=False)
    ariel_application_rating = auto_field(required=False)
    # add data validation
    instructor_rating = auto_field(required=False)
    instrument_rating = auto_field(required=False)
    low_level_rating = auto_field(required=False)
    night_vfr_rating = auto_field(required=False)
    night_visual_imaging_sys_rating = auto_field(required=False)

    user = ma.Nested("UserSchema")

    class Meta:
        model = Pilot
        load_instance = True

pilot_schema = PilotSchema()
multi_pilot_schema = PilotSchema(many=True)