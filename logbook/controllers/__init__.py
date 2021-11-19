from controllers.flight_controller import flights
from controllers.user_controller import users
from controllers.image_controller import flight_images

# Place that registers the controllers
registerable_controllers = [flights, users, flight_images]