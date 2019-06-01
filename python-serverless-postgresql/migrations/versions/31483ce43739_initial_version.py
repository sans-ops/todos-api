"""Initial version

Revision ID: 31483ce43739
Revises:
Create Date: 2019-06-01 11:56:11.114148

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '31483ce43739'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    connection = op.get_bind()
    connection.execute("CREATE EXTENSION IF NOT EXISTS pgcrypto;")


def downgrade():
    connection = op.get_bind()
    connection.execute("DROP EXTENSION IF EXISTS pgcrypto;")
