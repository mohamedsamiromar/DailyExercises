"""empty message

Revision ID: 2d76282f8a21
Revises: 297dcfc51e34
Create Date: 2022-10-15 18:03:50.676171

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2d76282f8a21'
down_revision = '297dcfc51e34'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', sa.String(length=120), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'email')
    # ### end Alembic commands ###
