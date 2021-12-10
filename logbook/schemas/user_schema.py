from main import ma
from models.users import User
from marshmallow_sqlalchemy import auto_field
from marshmallow import fields, exceptions, validate
from werkzeug.security import generate_password_hash

class UserSchema(ma.SQLAlchemyAutoSchema):
    """
    Creates instances from dictionaries and vice versa.
    """
    class Meta:
        model=User
        load_instance=True

    id = auto_field(dump_only=True)
    name = auto_field(required=True, validate=validate.Length(1))
    email = auto_field(required=True, validate=validate.Email())
    is_admin = auto_field(required=False, default=False)
    is_superadmin = auto_field(required=False, default=False)
    has_image = auto_field(default=False)
    password = fields.Method(
        required=True,
        load_only=True,
        deserialize="load_password"
    )

    def load_password(self, password):
        symbol = ['!','"','#','\'','$','%','&','(',')','*','+',',','-','.','/',':',';','<','=','>','?','@','[','\\',']','^','_','`','{','|','}','~']

        if len(password)>8:
            raise exceptions.ValidationError("Password must be at least 8 characters.")
        if len(password)>20:
            raise exceptions.ValidationError("Password must be no longer than 20 characters.")
        if not any(char.isdigit() for char in password):
            raise exceptions.ValidationError("Password must contain at least one number.")
        if not any(char.isupper() for char in password):
            raise exceptions.ValidationError("Password must contain at least one uppercase letter.")
        if not any(char.islower() for char in password):
            raise exceptions.ValidationError("Password must contain at least one lowercase letter.")
        if not any(char in symbol for char in password):
            raise exceptions.ValidationError("Password must contain at least one symbol.")
        return generate_password_hash(password, method='sha256')

user_schema = UserSchema()
multi_user_schema = UserSchema(many=True)
user_update_schema = UserSchema(partial=True)