from main import db

class Aircraft(db.Model):
    """
    A class to represent an aircraft model.
    ...
    Attributes
    ----------
    aircraft_id : int
        the primary key
    multi_engine : bool
        false for single engine true for multi engine
    type : str
        aircraft make and model
    nationality : str
        country of registration
    registration : str
        registration number
    """

    __tablename__ = "aircraft"

    aircraft_id = db.Column(db.Integer, primary_key=True)
    multi_engine = db.Column(db.Boolean, nullable=False, server_default=False)
    type = db.Column(db.String, nullable=False)
    nationality = db.Column(db.String, nullable=False, server_default="Australia")
    registration = db.Column(db.String, nullable=False, unique=True)