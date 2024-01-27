"""empty message

Revision ID: ea64dde9f554
Revises: e1114cee07d0
Create Date: 2024-01-27 00:41:47.997146

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ea64dde9f554'
down_revision: Union[str, None] = 'e1114cee07d0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('book', sa.Column('general_ratings', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('book', 'general_ratings')
    # ### end Alembic commands ###
