"""up1  completed

Revision ID: 3630b2579b7f
Revises: 42f2d577bce5
Create Date: 2023-07-31 21:10:57.202093

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3630b2579b7f'
down_revision = '42f2d577bce5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('contacts', 'first_name',
               existing_type=sa.VARCHAR(length=150),
               nullable=True)
    op.alter_column('contacts', 'last_name',
               existing_type=sa.VARCHAR(length=150),
               nullable=True)
    op.alter_column('contacts', 'email',
               existing_type=sa.VARCHAR(length=150),
               nullable=True)
    op.alter_column('contacts', 'phone_number',
               existing_type=sa.VARCHAR(length=150),
               nullable=True)
    op.alter_column('contacts', 'birthday',
               existing_type=sa.DATE(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('contacts', 'birthday',
               existing_type=sa.DATE(),
               nullable=False)
    op.alter_column('contacts', 'phone_number',
               existing_type=sa.VARCHAR(length=150),
               nullable=False)
    op.alter_column('contacts', 'email',
               existing_type=sa.VARCHAR(length=150),
               nullable=False)
    op.alter_column('contacts', 'last_name',
               existing_type=sa.VARCHAR(length=150),
               nullable=False)
    op.alter_column('contacts', 'first_name',
               existing_type=sa.VARCHAR(length=150),
               nullable=False)
    # ### end Alembic commands ###
