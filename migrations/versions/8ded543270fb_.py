"""empty message

Revision ID: 8ded543270fb
Revises: 10bc41d3f796
Create Date: 2024-03-21 15:14:19.155849

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ded543270fb'
down_revision = '10bc41d3f796'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('characters', schema=None) as batch_op:
        batch_op.drop_constraint('characters_homeworld_id_fkey', type_='foreignkey')
        batch_op.drop_column('homeworld_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('characters', schema=None) as batch_op:
        batch_op.add_column(sa.Column('homeworld_id', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.create_foreign_key('characters_homeworld_id_fkey', 'planets', ['homeworld_id'], ['id'])

    # ### end Alembic commands ###