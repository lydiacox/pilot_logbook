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
    flight_no : list
        1:M relationship with flights
    """

    __tablename__ = "aircraft"

    aircraft_id = db.Column(db.Integer, primary_key=True)
    multi_engine = db.Column(db.Boolean, nullable=False, server_default="False")
    type = db.Column(db.String, nullable=False)
    # extention project: make nationality & registration in combination unique
    # define validation of the schema as a whole
    # https://marshmallow.readthedocs.io/en/latest/extending.html#schema-level-validation
    nationality = db.Column(db.String, nullable=False, server_default="Australia")
    registration = db.Column(db.String, nullable=False)
    # One to many relationship, bi-directional, to flights (parent)
    flight_no = db.relationship("Flight", back_populates="aircraft", lazy="joined")