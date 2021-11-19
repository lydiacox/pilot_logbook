from flask import Blueprint, request, redirect, abort, url_for, current_app
from pathlib import Path
from models.users import User
import boto3

user_images = Blueprint("user_images", __name__)

@user_images.route("/users/account/image/", methods=["POST"])
def update_image(id):
    user = User.query.get_or_404(id)

    if "image" in request.files:
        image = request.files["image"]

        # Interprets a string as an address in memory        
        if Path(image.filename).suffix != ".png":
            return abort(400, description="Invalid file type")

        bucket = boto3.resource("s3").Bucket(current_app.config["AWS_S3_BUCKET"])
        bucket.upload_fileobj(image, user.image_filename)

        return redirect(url_for("users.user_detail", id=id))
    
    return abort(400, description="No image")