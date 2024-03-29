"""empty message

Revision ID: 8b696e068598
Revises: 2d76282f8a21
Create Date: 2022-10-15 18:05:52.389538

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8b696e068598'
down_revision = '2d76282f8a21'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('daily_exercise',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('exercise_name', sa.String(), nullable=False),
    sa.Column('exercise_start_date', sa.DateTime(), nullable=True),
    sa.Column('exercise_end_date', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('daily_exercise')
    # ### end Alembic commands ###
