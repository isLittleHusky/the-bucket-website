"""empty message

Revision ID: be47746dfa5d
Revises: cde510685d1c
Create Date: 2019-08-29 13:38:14.298543

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'be47746dfa5d'
down_revision = 'cde510685d1c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'is_admin')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('is_admin', sa.BOOLEAN(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###