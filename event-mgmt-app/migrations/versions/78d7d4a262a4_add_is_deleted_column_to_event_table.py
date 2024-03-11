"""Add is_deleted column to Event table

Revision ID: 78d7d4a262a4
Revises: 3c92832be9bc
Create Date: 2024-02-13 22:12:20.461775

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '78d7d4a262a4'
down_revision = '3c92832be9bc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('event', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_deleted', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('event', schema=None) as batch_op:
        batch_op.drop_column('is_deleted')

    # ### end Alembic commands ###