from main import ma
from models.pilot import Pilot
from marshmallow_sqlalchemy import auto_field

class PilotSchema(ma.SQLAlchemyAutoSchema):
    pilot_id = auto_field(dump_only=True)

    class Meta:
        model = Pilot
        load_instance = True

pilot_schema = PilotSchema()
pilots_schema = PilotSchema(many=True)