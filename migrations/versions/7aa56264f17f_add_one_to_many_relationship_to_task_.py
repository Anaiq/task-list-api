"""add one to many relationship to Task and Goal models

Revision ID: 7aa56264f17f
Revises: 3167640fa619
Create Date: 2022-11-09 18:57:29.067020

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7aa56264f17f'
down_revision = '3167640fa619'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('task_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'task', 'task', ['task_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'task', type_='foreignkey')
    op.drop_column('task', 'task_id')
    # ### end Alembic commands ###
