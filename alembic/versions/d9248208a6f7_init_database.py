"""init database

Revision ID: d9248208a6f7
Revises:
Create Date: 2023-04-28 15:10:51.000163

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects.postgresql import UUID

# revision identifiers, used by Alembic.
revision = 'd9248208a6f7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "user",
        sa.Column("id", UUID, nullable=False),
        sa.Column("email", sa.String, nullable=False, unique=True, index=True),
        sa.Column("name", sa.String, nullable=False),
        sa.Column("created_at", sa.DateTime, nullable=False),
        sa.Column("updated_at", sa.DateTime, nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "country",
        sa.Column("id", UUID, nullable=False, index=True),
        sa.Column("name", sa.String, nullable=False),
        sa.Column("created_at", sa.DateTime, nullable=False),
        sa.Column("updated_at", sa.DateTime, nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_table(
        "user_country_link",
        sa.Column("user_id", UUID, nullable=False, index=True),
        sa.Column("country_id", UUID, nullable=False, index=True),
        sa.Column("created_at", sa.DateTime, nullable=False),
        sa.PrimaryKeyConstraint("user_id", "country_id"),
        sa.ForeignKeyConstraint(["user_id"], ["user.id"]),
        sa.ForeignKeyConstraint(["country_id"], ["country.id"]),
    )


def downgrade() -> None:
    op.drop_table("user_country_link")
    op.drop_table("country")
    op.drop_table("user")
