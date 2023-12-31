"""Create  tables

Revision ID: 62efa76c01a2
Revises: d1a702ba1094
Create Date: 2023-08-05 10:34:21.447608

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '62efa76c01a2'
down_revision = 'd1a702ba1094'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('payments', schema=None) as batch_op:
        batch_op.add_column(sa.Column('payment_method', sa.String(length=50), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('payments', schema=None) as batch_op:
        batch_op.drop_column('payment_method')

    # ### end Alembic commands ###
