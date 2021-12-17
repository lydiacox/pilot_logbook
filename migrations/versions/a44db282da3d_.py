"""empty message

Revision ID: a44db282da3d
Revises: 
Create Date: 2021-12-17 13:03:59.044568

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a44db282da3d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('aircraft',
    sa.Column('aircraft_id', sa.Integer(), nullable=False),
    sa.Column('multi_engine', sa.Boolean(), server_default='False', nullable=False),
    sa.Column('type', sa.String(), nullable=False),
    sa.Column('nationality', sa.String(), server_default='Australia', nullable=False),
    sa.Column('registration', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('aircraft_id')
    )
    op.create_table('flasklogin-users',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=100), nullable=False),
    sa.Column('last_name', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=40), nullable=False),
    sa.Column('password', sa.String(length=200), nullable=False),
    sa.Column('is_admin', sa.Boolean(), server_default='False', nullable=False),
    sa.Column('is_superadmin', sa.Boolean(), server_default='False', nullable=False),
    sa.Column('has_image', sa.Boolean(), server_default='False', nullable=False),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('flights',
    sa.Column('flight_id', sa.Integer(), nullable=False),
    sa.Column('date_began', sa.DateTime(), server_default='1/1/1900', nullable=False),
    sa.Column('take_off_landing_points', sa.String(length=200), nullable=False),
    sa.Column('pilot_in_command', sa.String(length=100), nullable=False),
    sa.Column('other_crew', sa.String(length=200), nullable=True),
    sa.Column('single_engine_icus_day', sa.Float(precision=1), nullable=True),
    sa.Column('single_engine_icus_night', sa.Float(precision=1), nullable=True),
    sa.Column('single_engine_dual_day', sa.Float(precision=1), nullable=True),
    sa.Column('single_engine_dual_night', sa.Float(precision=1), nullable=True),
    sa.Column('single_engine_command_day', sa.Float(precision=1), nullable=True),
    sa.Column('single_engine_command_night', sa.Float(precision=1), nullable=True),
    sa.Column('multi_engine_icus_day', sa.Float(precision=1), nullable=True),
    sa.Column('multi_engine_icus_night', sa.Float(precision=1), nullable=True),
    sa.Column('multi_engine_dual_day', sa.Float(precision=1), nullable=True),
    sa.Column('multi_engine_dual_night', sa.Float(precision=1), nullable=True),
    sa.Column('multi_engine_command_day', sa.Float(precision=1), nullable=True),
    sa.Column('multi_engine_command_night', sa.Float(precision=1), nullable=True),
    sa.Column('multi_engine_co_pilot_day', sa.Float(precision=1), nullable=True),
    sa.Column('multi_engine_co_pilot_night', sa.Float(precision=1), nullable=True),
    sa.Column('instrument_in_flight', sa.Float(precision=1), nullable=True),
    sa.Column('instrument_ground', sa.Float(precision=1), nullable=True),
    sa.Column('creator_id', sa.Integer(), nullable=True),
    sa.Column('aircraft_flight_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['aircraft_flight_id'], ['aircraft.aircraft_id'], ),
    sa.ForeignKeyConstraint(['creator_id'], ['flasklogin-users.user_id'], ),
    sa.PrimaryKeyConstraint('flight_id')
    )
    op.create_table('pilot',
    sa.Column('pilot_id', sa.Integer(), nullable=False),
    sa.Column('arn', sa.Integer(), nullable=True),
    sa.Column('licence_class', sa.String(length=10), nullable=True),
    sa.Column('ariel_application_rating', sa.Boolean(), server_default='False', nullable=True),
    sa.Column('instructor_rating', sa.String(length=10), nullable=True),
    sa.Column('instrument_rating', sa.Boolean(), server_default='False', nullable=True),
    sa.Column('low_level_rating', sa.Boolean(), server_default='False', nullable=True),
    sa.Column('night_vfr_rating', sa.Boolean(), server_default='False', nullable=True),
    sa.Column('night_visual_imaging_sys_rating', sa.Boolean(), server_default='False', nullable=True),
    sa.Column('parent_user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['parent_user_id'], ['flasklogin-users.user_id'], ),
    sa.PrimaryKeyConstraint('pilot_id')
    )
    op.create_table('instrument_approach',
    sa.Column('approach_id', sa.Integer(), nullable=False),
    sa.Column('approach_type', sa.String(), nullable=False),
    sa.Column('approach_flight_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['approach_flight_id'], ['flights.flight_id'], ),
    sa.PrimaryKeyConstraint('approach_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('instrument_approach')
    op.drop_table('pilot')
    op.drop_table('flights')
    op.drop_table('flasklogin-users')
    op.drop_table('aircraft')
    # ### end Alembic commands ###
