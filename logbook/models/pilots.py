from main import db
from sqlalchemy import ChoiceTypes

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
    ariel_application_rating : bool
    instructor_rating : str
        grade 1, grade 2 or grade 3
    instrument_rating : bool
    low_level_rating : bool
    night_vfr_rating : bool
    night_visual_imaging_sys_rating : bool
    user : int
        user_id field from the users model
    """
    # Uncomment if using enum or ClassType for data validation
    # https://sqlalchemy-utils.readthedocs.io/en/latest/data_types.html
    # https://docs.sqlalchemy.org/en/14/core/type_basics.html#sqlalchemy.types.Enum
    # classes = [
    #     (u'rpl', u'RPL'),
    #     (u'ppl', u'PPL'),
    #     (u'cpl', u'CPL'),
    #     (u'atpl', u'ATPL')
    # ]
    # ratings = [
    #     (u'grade 1', u'Grade 1'),
    #     (u'grade 2', u'Grade 2'),
    #     (u'grade 3', u'Grade 3')
    # ]
    __table__name = "pilots"

    pilot_id = db.Column(db.Integer, primary_key=True)
    arn = db.Column(db.Integer(), nullable=True)
    licence_class = db.Column(db.String(10), nullable=True)
    ariel_application_rating = db.Column(db.Boolean, nullable=True, server_default=False)
    instructor_rating = db.Column(db.String(10), nullable=True)
    instrument_rating = db.Column(db.Boolean, nullable=True)
    low_level_rating = db.Column(db.Boolean, nullable=True)
    night_vfr_rating = db.Column(db.Boolean, nullable=True)
    night_visual_imaging_sys_rating = db.Column(db.Boolean, nullable=True)

    user = db.Column(db.Integer, db.ForeignKey("flasklogin-users.user_id"))