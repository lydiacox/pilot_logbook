from main import db
from flask import Blueprint

db_commands = Blueprint("db-custom", __name__)

@db_commands.cli.command("logbookdb")
def logbookdb():
    """Create a new "logbookdb" database"""
    db.engine.execute("CREATE DATABASE logbookdb;")
    print("Database created!")

@db_commands.cli.command("create")
def create_db():
    """Creates tables in the database based on the models."""
    db.create_all()
    print("Tables created!")

@db_commands.cli.command("drop")
def drop_db():
    """Drops all tables in the database."""
    db.drop_all()
    db.engine.execute("DROP TABLE IF EXISTS alembic_version;")
    print("Tables deleted!")

@db_commands.cli.command("seed")
def seed_db():
    """Seeds the table/"""
    from models.flights import Flight
    from faker import Faker
    from schemas.flight_schema import flight_schema
    faker = Faker()

    for i in range(2):
        # hand over required fields for flight object
        flight = flight_schema.load({"date_began": '2021-07-05T12:36:52.933000', "take_off_landing_points": faker.catch_phrase(), "pilot_in_command": faker.catch_phrase()})
        db.session.add(flight)

    db.session.commit()
    print("Tables seeded!")

@db_commands.cli.command("reset")
def reset_db():
    """Drops, creates and seeds tables in one step."""
    db.drop_all()
    db.engine.execute("DROP TABLE IF EXISTS alembic_version;")
    print("Tables deleted!")
    db.create_all()
    print("Tables created!")
    from models.flights import Flight
    from schemas.flight_schema import flight_schema
    from faker import Faker
    faker = Faker()

    for i in range(22):
        flight = flight_schema.load({"date_began": '2021-07-05T12:36:52.933000', "take_off_landing_points": faker.catch_phrase(), "pilot_in_command": faker.catch_phrase()})
        db.session.add(flight)

    db.session.commit()
    print("Tables seeded!")