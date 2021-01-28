"""initial

Revision ID: 53c6eb5b4ff8
Revises: 
Create Date: 2021-01-25 21:55:33.943283

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '53c6eb5b4ff8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('district',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('surface', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('magnitude',
    sa.Column('id', sa.String(length=10), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('formula', sa.String(length=5), nullable=False),
    sa.Column('measurement_unit', sa.String(length=10), nullable=False),
    sa.Column('measurement_technique', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pollution_station',
    sa.Column('code', sa.String(length=20), nullable=False),
    sa.Column('address', sa.String(length=100), nullable=True),
    sa.Column('start_date', sa.DateTime(), nullable=False),
    sa.Column('end_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('code')
    )
    op.create_table('neighborhood',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('surface', sa.Float(), nullable=True),
    sa.Column('district_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['district_id'], ['district.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('pollution_measurement',
    sa.Column('province', sa.Integer(), nullable=False),
    sa.Column('town', sa.Integer(), nullable=False),
    sa.Column('station', sa.Integer(), nullable=False),
    sa.Column('datetime', sa.DateTime(), nullable=False),
    sa.Column('magnitude', sa.Integer(), nullable=False),
    sa.Column('method', sa.Integer(), nullable=False),
    sa.Column('analysis_period', sa.Integer(), nullable=False),
    sa.Column('data', sa.Float(), nullable=False),
    sa.Column('validation_code', sa.String(length=1), nullable=False),
    sa.Column('station_id', sa.String(length=20), nullable=False),
    sa.ForeignKeyConstraint(['station_id'], ['pollution_station.code'], ),
    sa.PrimaryKeyConstraint('province', 'town', 'station', 'datetime', 'magnitude')
    )
    op.create_table('density',
    sa.Column('district_id', sa.Integer(), nullable=False),
    sa.Column('neighborhood_id', sa.Integer(), nullable=False),
    sa.Column('year', sa.Integer(), nullable=False),
    sa.Column('month', sa.Integer(), nullable=False),
    sa.Column('value', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['district_id'], ['district.id'], ),
    sa.ForeignKeyConstraint(['neighborhood_id'], ['neighborhood.id'], ),
    sa.PrimaryKeyConstraint('district_id', 'neighborhood_id', 'year', 'month')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('density')
    op.drop_table('pollution_measurement')
    op.drop_table('neighborhood')
    op.drop_table('pollution_station')
    op.drop_table('magnitude')
    op.drop_table('district')
    # ### end Alembic commands ###
