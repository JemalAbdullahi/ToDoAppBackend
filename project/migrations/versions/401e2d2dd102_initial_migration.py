"""Initial Migration

Revision ID: 401e2d2dd102
Revises: 
Create Date: 2021-03-31 12:09:48.151131

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '401e2d2dd102'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('groups',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('group_key', sa.String(), nullable=True),
    sa.Column('is_public', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('group_key')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstname', sa.String(), nullable=True),
    sa.Column('lastname', sa.String(), nullable=True),
    sa.Column('phonenumber', sa.String(length=15), nullable=True),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('password', sa.String(length=128), nullable=True),
    sa.Column('emailaddress', sa.String(length=120), nullable=True),
    sa.Column('api_key', sa.String(), nullable=True),
    sa.Column('avatar', sa.LargeBinary(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('phonenumber'),
    sa.UniqueConstraint('username')
    )
    op.create_table('group_member',
    sa.Column('group_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['group_id'], ['groups.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE')
    )
    op.create_table('tasks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('index', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('note', sa.String(), nullable=True),
    sa.Column('completed', sa.Boolean(), nullable=False),
    sa.Column('repeats', sa.String(), nullable=True),
    sa.Column('reminders', sa.String(), nullable=True),
    sa.Column('group_id', sa.Integer(), nullable=True),
    sa.Column('task_key', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['group_id'], ['groups.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('task_key')
    )
    op.create_table('subtasks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('task_id', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('note', sa.String(), nullable=True),
    sa.Column('completed', sa.Boolean(), nullable=False),
    sa.Column('repeats', sa.String(), nullable=True),
    sa.Column('reminders', sa.String(), nullable=True),
    sa.Column('group', sa.String(), nullable=True),
    sa.Column('index', sa.Integer(), nullable=True),
    sa.Column('subtask_key', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['task_id'], ['tasks.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('subtask_key')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('subtasks')
    op.drop_table('tasks')
    op.drop_table('group_member')
    op.drop_table('users')
    op.drop_table('groups')
    # ### end Alembic commands ###
