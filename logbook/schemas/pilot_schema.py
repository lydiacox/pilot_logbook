from marshmallow import validate
from main import ma
from models.pilot import Pilot
from marshmallow_sqlalchemy import auto_field
from marshmallow.validate import Length

class PilotSchema(ma.SQLAlchemyAutoSchema):
    pilot_id = auto_field(dump_only=True)
    pilot_name = auto_field(required=True, validate=Length(min=1, max=100))

    class Meta:
        model = Pilot
        load_instance = True

pilot_schema = PilotSchema()
pilots_schema = PilotSchema(many=True)