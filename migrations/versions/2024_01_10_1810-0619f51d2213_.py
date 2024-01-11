"""empty message

Revision ID: 0619f51d2213
Revises: a154b6dbeecb
Create Date: 2024-01-10 18:10:13.589828

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0619f51d2213'
down_revision: Union[str, None] = 'a154b6dbeecb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'book', ['url'])
    op.add_column('user', sa.Column('profile_image', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'profile_image')
    op.drop_constraint(None, 'book', type_='unique')
    # ### end Alembic commands ###
