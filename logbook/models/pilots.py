from sqlalchemy.orm import relationship
from main import db

class Pilot(db.Model):
    """
    A class to represent a pilot model.
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
        whether the pilot has an arial application rating
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
    user : 
        1:1 relationship with the user
    """

    __table__name = "pilots"

    pilot_id = db.Column(db.Integer, primary_key=True)
    arn = db.Column(db.Integer(), nullable=True)
    licence_class = db.Column(db.String(10), nullable=True)
    aerial_application_rating = db.Column(db.Boolean, nullable=True, server_default="False")
    instructor_rating = db.Column(db.String(10), nullable=True)
    instrument_rating = db.Column(db.Boolean, nullable=True, server_default="False")
    low_level_rating = db.Column(db.Boolean, nullable=True, server_default="False")
    night_vfr_rating = db.Column(db.Boolean, nullable=True, server_default="False")
    night_visual_imaging_sys_rating = db.Column(db.Boolean, nullable=True, server_default="False")
    # One to one relationship to users (child)
    parent_user_id = db.Column(db.Integer, db.ForeignKey('flasklogin-users.user_id'))
    user = db.relationship("User", back_populates="pilot", lazy="joined")