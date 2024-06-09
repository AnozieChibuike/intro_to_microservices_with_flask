"""empty message

Revision ID: 7d7f8524710d
Revises: 
Create Date: 2024-06-09 23:44:12.664064

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7d7f8524710d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todos',
    sa.Column('user_id', sa.String(length=100), nullable=False),
    sa.Column('task', sa.String(length=100), nullable=False),
    sa.Column('completed', sa.Boolean(), nullable=True),
    sa.Column('id', sa.String(length=126), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('todos')
    # ### end Alembic commands ###
