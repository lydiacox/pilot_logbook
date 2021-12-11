from main import db
from flask_login import UserMixin
from werkzeug.security import check_password_hash

class User(UserMixin, db.Model):
    """
    A class to represent a user model.
    ...
    Attributes
    ----------
    user_id : int
        the primary key
    pilot_id : int
        the foreign key for the pilot_profile
    first_name : string
        first name of the user
    last_name : string
        last name of the user
    email : string
        email address of the user
    password : string
        password of the user
    is_admin : boolean
        whether the user is an admin
    is_superadmin : boolean
        whether the user is a super admin
    has_image
        whether the user has uploaded a profile image
    Methods
    -------
    check_password(password):
        Validates a password against the hashed password value.
    image_filename():
        Creates the file name for the user's uploaded image.
    """
    __tablename__ = "flasklogin-users"
    user_id = db.Column(
        db.Integer,
        primary_key=True
    )
    first_name = db.Column(
        db.String(100),
        nullable=False
    )
    last_name = db.Column(
        db.String(100),
        nullable=False
    )
    email = db.Column(
        db.String(40),
        unique=True,
        nullable=False
    )
    password = db.Column(
        db.String(40),
        nullable=False
    )
    is_admin = db.Column(
        db.Boolean(),
        nullable=False,
        server_default="False"
    )

    is_superadmin = db.Column(
        db.Boolean(),
        nullable=False,
        server_default="False"
    )
        
    has_image = db.Column(
        db.Boolean(),
        nullable=False,
        server_default="False"
    )
    flights = db.relationship(
        "Flight",
        backref="creator",
        lazy="joined"
    )
    pilot = db.relationship(
        "Pilot",
        backref="user",
        lazy="joined"
    )
    # To access the list of flights created by a user, we call
    # Username.flights = [<Flight 1>, <Flight 2>]
    # To access the creator of a flight, we call Flightno.creator
    # = <User name>

    def check_password(self, password):
        """
        Validates a password against the hashed password value.
            Parameters:
                password: The password as input by the user.
            Returns:
                boolean
        """
        return check_password_hash(self.password, password)

    @property
    def image_filename(self):
        """
        Creates the file name for the user's uploaded image.
            Parameters:
                None
            Returns:
                A string with the image file name
        """
        return f"user_images/{self.user_id}.png"
    