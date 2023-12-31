"""  completed

Revision ID: ad75ba5df62a
Revises: b7dda38239e5
Create Date: 2023-07-31 22:34:49.440550

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ad75ba5df62a'
down_revision = 'b7dda38239e5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('contacts', sa.Column('created_date', sa.Date(), nullable=True))
    op.drop_column('contacts', 'extra_data')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('contacts', sa.Column('extra_data', sa.VARCHAR(length=150), autoincrement=False, nullable=True))
    op.drop_column('contacts', 'created_date')
    # ### end Alembic commands ###
