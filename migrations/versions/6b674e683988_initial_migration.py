"""initial migration

Revision ID: 6b674e683988
Revises: 42b413b5993e
Create Date: 2017-11-08 20:21:54.908698

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b674e683988'
down_revision = '42b413b5993e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('asks', sa.Column('actual_time', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('asks', 'actual_time')
    # ### end Alembic commands ###
