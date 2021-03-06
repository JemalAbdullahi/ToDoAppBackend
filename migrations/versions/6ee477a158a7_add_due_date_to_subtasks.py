"""Add due date to subtasks

Revision ID: 6ee477a158a7
Revises: 365c623b1e03
Create Date: 2021-06-20 16:10:22.987801

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6ee477a158a7'
down_revision = '365c623b1e03'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('subtasks', sa.Column('due_date', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('subtasks', 'due_date')
    # ### end Alembic commands ###
