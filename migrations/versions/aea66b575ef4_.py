"""empty message

Revision ID: aea66b575ef4
Revises: b595640905f1
Create Date: 2021-01-24 19:33:53.634864

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'aea66b575ef4'
down_revision = 'b595640905f1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('artists', 'genres',
               existing_type=postgresql.ARRAY(sa.VARCHAR(length=32)),
               nullable=True)
    op.alter_column('venues', 'genres',
               existing_type=postgresql.ARRAY(sa.VARCHAR(length=32)),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('venues', 'genres',
               existing_type=postgresql.ARRAY(sa.VARCHAR(length=32)),
               nullable=False)
    op.alter_column('artists', 'genres',
               existing_type=postgresql.ARRAY(sa.VARCHAR(length=32)),
               nullable=False)
    # ### end Alembic commands ###
