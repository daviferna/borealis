"""initial

Revision ID: 05ba1496d4df
Revises: 
Create Date: 2021-01-18 20:04:14.108207

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '05ba1496d4df'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('magnitude',
    sa.Column('id', sa.String(length=10), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('formula', sa.String(length=5), nullable=False),
    sa.Column('measurement_unit', sa.String(length=10), nullable=False),
    sa.Column('measurement_technique', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('station',
    sa.Column('code', sa.String(length=20), nullable=False),
    sa.Column('address', sa.String(length=100), nullable=True),
    sa.Column('start_date', sa.DateTime(), nullable=False),
    sa.Column('end_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('code')
    )
    op.create_table('measurement',
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
    sa.ForeignKeyConstraint(['station_id'], ['station.code'], ),
    sa.PrimaryKeyConstraint('province', 'town', 'station', 'datetime', 'magnitude')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('measurement')
    op.drop_table('station')
    op.drop_table('magnitude')
    # ### end Alembic commands ###
