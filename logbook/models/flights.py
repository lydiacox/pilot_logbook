from main import db

# Tells the ORM what tables should exist in teh database
# Allows us to retrieve info from those tables
class Flight(db.Model):
    __tablename__ = "flights"
    flight_id = db.Column(db.Integer, primary_key=True)
    aircraft_type = db.Column(db.String(20), server_default="Wright Flyer")
    aircraft_rego = db.Column(db.String(10), server_default="AAAA")
    flight_date = db.Column(db.String(10), nullable=False, server_default="1/1/1900")
    pilot_in_command = db.Column(db.String(100), nullable=False)
    other_crew = db.Column(db.String(200))
    details = db.Column(db.String(200), nullable=False)
    single_engine_icus_day = db.Column(db.Float)
    single_engine_icus_night = db.Column(db.Float)
    single_engine_dual_day = db.Column(db.Float)
    single_engine_dual_night = db.Column(db.Float)
    single_engine_command_day = db.Column(db.Float)
    single_engine_command_night = db.Column(db.Float)
    multi_engine_icus_day = db.Column(db.Float)
    multi_engine_icus_night = db.Column(db.Float)
    multi_engine_dual_day = db.Column(db.Float)
    multi_engine_dual_night = db.Column(db.Float)
    multi_engine_command_day = db.Column(db.Float)
    multi_engine_command_night = db.Column(db.Float)
    multi_engine_co_pilot_day = db.Column(db.Float)
    multi_engine_co_pilot_night = db.Column(db.Float)
    instrument_in_flight = db.Column(db.Float)
    instrument_ground = db.Column(db.Float)

    @property
    def image_filename(self):
        return f"flight_images/{self.flight_id}.png"