"""empty message

Revision ID: 24dd730699bb
Revises: 9b364f5d7e9f
Create Date: 2024-04-19 10:11:06.452823

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24dd730699bb'
down_revision = '9b364f5d7e9f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('favorite_planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('planets_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['planets_id'], ['planets.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favorite_planets')
    # ### end Alembic commands ###
