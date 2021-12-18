from main import ma
from models.pilots import Pilot
from marshmallow_sqlalchemy import auto_field
from marshmallow import validate

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
    aerial_application_rating : bool
    instructor_rating : str
        grade 1, grade 2 or grade 3
    instrument_rating : bool
        whether the pilot has an instrument rating
    low_level_rating : bool
        whether the pilot has a low level rating
    night_vfr_rating : bool
        whether the pilot has a night vfr rating
    night_visual_imaging_sys_rating : bool
        whether the pilot has aa night visual imaging system rating
    parent_user_id : int
        foreign key for the related user
    user : dict
        nested UserSchema
    """
    class Meta:
        model = Pilot
        load_instance = True

    pilot_id = auto_field(dump_only=True)
    arn = auto_field(required=False)
    # add data validation
    licence_class = auto_field(required=False)
    # fix spelling of "aerial"
    aerial_application_rating = auto_field(required=False)
    # add data validation
    instructor_rating = auto_field(required=False)
    instrument_rating = auto_field(required=False)
    low_level_rating = auto_field(required=False)
    night_vfr_rating = auto_field(required=False)
    night_visual_imaging_sys_rating = auto_field(required=False)
    parent_user_id = auto_field(required=True)
    user = ma.Nested("UserSchema")

pilot_schema = PilotSchema()
multi_pilot_schema = PilotSchema(many=True)
pilot_update_schema = PilotSchema(partial=True)