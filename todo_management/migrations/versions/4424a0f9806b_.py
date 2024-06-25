"""empty message

Revision ID: 4424a0f9806b
Revises: 2f51601d2782
Create Date: 2024-06-24 08:05:26.386265

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4424a0f9806b'
down_revision = '2f51601d2782'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('todos', schema=None) as batch_op:
        batch_op.add_column(sa.Column('title', sa.String(length=100), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('todos', schema=None) as batch_op:
        batch_op.drop_column('title')

    # ### end Alembic commands ###
