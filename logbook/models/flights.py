from main import db

class Flight(db.Model):
    __tablename__ = "flights"
    flight_id = db.Column(db.Integer, primary_key=True)
    flight_no = db.Column(db.String(10), nullable=False)

    def __init__(self, flight_no):
        self.flight_no = flight_no