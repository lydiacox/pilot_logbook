from flask import Blueprint, request, redirect, abort, url_for, current_app
from pathlib import Path
from models.flights import Flight
import boto3

flight_images = Blueprint("flight_images", __name__)

@flight_images.route("/flights/<int:id>/image/", methods=["POST"])
def update_image(id):
    flight = Flight.query.get_or_404(id)

    if "image" in request.files:
        image = request.files["image"]

        # Interprets a string as an address in memory        
        if Path(image.filename).suffix != ".png":
            return abort(400, description="Invalid file type")

        bucket = boto3.resource("s3").Bucket(current_app.config["AWS_S3_BUCKET"])
        bucket.upload_fileobj(image, flight.image_filename)

        return redirect(url_for("flights.get_flight", id=id))
    
    return abort(400, description="No image")