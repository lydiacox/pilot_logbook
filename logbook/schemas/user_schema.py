from enum import auto
from typing_extensions import Required
from main import ma
from models.users import User
from marshmallow_sqlalchemy import auto_field
from marshmallow import fields, exceptions, validate
from werkzeug.security import generate_password_hash

class UserSchema(ma.SQLAlchemyAutoSchema):
    """
    A class to represent a user schema.
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
    load_password(password):
        Validates and hashes the password.
    """
    class Meta:
        model=User
        load_instance=True

    user_id = auto_field(dump_only=True)
    first_name = auto_field(required=True, validate=validate.Length(1))
    last_name = auto_field(required=True, validate=validate.Length(1))
    email = auto_field(required=True, validate=validate.Email())
    password = fields.Method(
        required=True,
        load_only=True,
        deserialize="load_password"
    )
    is_admin = auto_field(required=False, default=False)
    is_superadmin = auto_field(required=False, default=False)
    has_image = auto_field(required=False, default=False)

    def load_password(self, password):
        """
        Validates the password, returns a hash of it.

        Passwords must be between 8 and 20 characters and contain at least one uppercase letter,
        one lowercase letter, one number and one symbol. They also cannot contain "password"
        or "passw0rd".
            Parameters:
                password: The user's desired password
            Returns:
                generate_password_hash: A 256-bit hash of the password
        """
        symbol = ['!','"','#','\'','$','%','&','(',')','*','+',',','-','.','/',':',';','<','=','>','?','@','[','\\',']','^','_','`','{','|','}','~']

        if len(password)>8:
            raise exceptions.ValidationError("Password must be at least 8 characters.")
        if len(password)>30:
            raise exceptions.ValidationError("Password must be no longer than 30 characters.")
        if not any(char.isdigit() for char in password):
            raise exceptions.ValidationError("Password must contain at least one number.")
        if not any(char.isupper() for char in password):
            raise exceptions.ValidationError("Password must contain at least one uppercase letter.")
        if not any(char.islower() for char in password):
            raise exceptions.ValidationError("Password must contain at least one lowercase letter.")
        if not any(char in symbol for char in password):
            raise exceptions.ValidationError("Password must contain at least one symbol.")
        if "password" or "passw0rd" in password.lower():
            raise exceptions.ValidationError("C'mon. No. You stop that now.")
        return generate_password_hash(password, method='sha256')
        # Alternatively, import regex package
        # www.geeksforgeeks.org/password-validation-in-python

user_schema = UserSchema()
multi_user_schema = UserSchema(many=True)
user_update_schema = UserSchema(partial=True)