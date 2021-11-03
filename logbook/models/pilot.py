from main import db

class Pilot(db.Model):
        __tablename__ = "pilots"
        pilot_id = db.Column(db.Integer, primary_key=True)
        pilot_name = db.Column(db.String(100), nullable=False)

        def __init__(self, pilot_id):
            self.pilot_id = pilot_id

        @property
        def serialize(self):
            return {
                "pilot_id": self.pilot_id,
                "pilot_name": self.pilot_name
            }