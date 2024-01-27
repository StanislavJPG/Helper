"""empty message

Revision ID: a439a276ef6c
Revises: 8b6c60baf203
Create Date: 2024-01-27 21:38:51.597809

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a439a276ef6c'
down_revision: Union[str, None] = '8b6c60baf203'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('rating', 'title')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('rating', sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
