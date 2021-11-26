from main import db
from flask_login import UserMixin
from werkzeug.security import check_password_hash

class User(UserMixin, db.Model):
    # tablename specifies the name of the table
    __tablename__ = "flasklogin-users"
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    name = db.Column(
        db.String(100),
        nullable=False
    )
    email = db.Column(
        db.String(40),
        unique=True,
        nullable=False
    )
    password = db.Column(
        db.String(200),
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
    # To access the list of flights created by a user, we call
    # Username.flights = [<Flight 1>, <Flight 2>]
    # To access the creator of a flight, we call Flightno.creator
    # = <User name>

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @property
    def image_filename(self):
        return f"user_images/{self.id}.png"
    