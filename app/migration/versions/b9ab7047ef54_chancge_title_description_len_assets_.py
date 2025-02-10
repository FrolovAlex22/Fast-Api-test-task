"""chancge title, description len assets table 2

Revision ID: b9ab7047ef54
Revises: c31c1e12a206
Create Date: 2025-02-10 11:04:08.394560

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b9ab7047ef54'
down_revision: Union[str, None] = 'c31c1e12a206'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('asset', 'title',
               existing_type=sa.VARCHAR(length=30),
               type_=sa.String(length=50),
               existing_nullable=False)
    op.alter_column('asset', 'description',
               existing_type=sa.VARCHAR(length=70),
               type_=sa.String(length=150),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('asset', 'description',
               existing_type=sa.String(length=150),
               type_=sa.VARCHAR(length=70),
               existing_nullable=False)
    op.alter_column('asset', 'title',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=30),
               existing_nullable=False)
    # ### end Alembic commands ###
