from main import db

# Tells the ORM what tables should exist in teh database
# Allows us to retrieve info from those tables
class Flight(db.Model):
    __tablename__ = "flights"
    flight_id = db.Column(db.Integer, primary_key=True)
    flight_no = db.Column(db.String(10), nullable=False)
    aircraft_type = db.Column(db.String(20), server_default="Wright Flyer")
    aircraft_call_letters = db.Column(db.String(10), server_default="AAAA")
    flight_date = db.Column(db.String(10), nullable=False, server_default="1/1/1900")

    @property
    def image_filename(self):
        return f"flight_images/{self.flight_id}.png"