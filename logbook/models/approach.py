from sqlalchemy.orm import relationship
from main import db

class InstrumentApproach(db.Model):
    """
    A class to represent an instrument approach model.
    ...
    Attributes
    ----------
    ifr_approach_id : int
        the primary key
    approach_type : str
        ILS, RNP, VOR, NDB or Visual
    """

    __tablename__ = "instrument_approach"

    ifr_approach_id = db.Column(db.Integer, primary_key=True)
    approach_type = db.Column(db.String, nullable=False)
    # One to many relationship, bi-directional, to flights (child)
    approach_flight_id = db.Column(db.Integer, db.ForeignKey("flights.flight_id"))
    approach_flight = db.relationship("Flight", back_populates="approach")