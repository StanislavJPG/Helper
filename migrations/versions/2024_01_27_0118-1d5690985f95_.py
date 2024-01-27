"""empty message

Revision ID: 1d5690985f95
Revises: ea64dde9f554
Create Date: 2024-01-27 01:18:34.754059

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1d5690985f95'
down_revision: Union[str, None] = 'ea64dde9f554'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('book', 'general_ratings')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('book', sa.Column('general_ratings', sa.INTEGER(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
