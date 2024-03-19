"""empty message

Revision ID: 97948d233c07
Revises: 
Create Date: 2024-03-18 19:12:02.857471

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '97948d233c07'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('characters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=True),
    sa.Column('height', sa.String(length=250), nullable=True),
    sa.Column('mass', sa.String(length=250), nullable=True),
    sa.Column('hair_color', sa.String(length=250), nullable=True),
    sa.Column('skin_color', sa.String(length=250), nullable=True),
    sa.Column('eye_color', sa.String(length=250), nullable=True),
    sa.Column('birth_year', sa.String(length=250), nullable=True),
    sa.Column('gender', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=True),
    sa.Column('rotation_period', sa.String(length=250), nullable=True),
    sa.Column('orbital_period', sa.String(length=250), nullable=True),
    sa.Column('diameter', sa.String(length=250), nullable=True),
    sa.Column('climate', sa.String(length=250), nullable=True),
    sa.Column('gravity', sa.String(length=250), nullable=True),
    sa.Column('terrain', sa.String(length=250), nullable=True),
    sa.Column('surface_water', sa.String(length=250), nullable=True),
    sa.Column('population', sa.String(length=250), nullable=True),
    sa.Column('residents', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['residents'], ['characters.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('planets')
    op.drop_table('user')
    op.drop_table('characters')
    # ### end Alembic commands ###