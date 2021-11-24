from flask import Blueprint, request, redirect, abort, url_for, current_app
from pathlib import Path
from models.users import User
import boto3
from flask_login import login_required, current_user
from main import db

user_images = Blueprint("user_images", __name__)

@user_images.route("/users/account/image/", methods=["POST"])
@login_required
def update_image():
    # if not current_user.is_admin:
    #     abort(403, "You do not have permission!")
    
    user = User.query.get_or_404(current_user.id)

    if "image" in request.files:
        image = request.files["image"]

        # Interprets a string as an address in memory        
        if Path(image.filename).suffix != ".png":
            return abort(400, description="Invalid file type")

        bucket = boto3.resource("s3").Bucket(current_app.config["AWS_S3_BUCKET"])
        bucket.upload_fileobj(image, user.image_filename)
        user.has_image=True
        db.session.commit()

        return redirect(url_for("users.user_detail", id=current_user.id))
    
    return abort(400, description="No image")