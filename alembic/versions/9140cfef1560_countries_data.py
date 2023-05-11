"""countries data

Revision ID: 9140cfef1560
Revises: d9248208a6f7
Create Date: 2023-04-28 18:33:21.326117

"""
from datetime import datetime
from uuid import uuid4

from alembic import op

# revision identifiers, used by Alembic.
revision = '9140cfef1560'
down_revision = 'd9248208a6f7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    countries = [
        "Australia",
        "Bangladesh",
        "Brunei",
        "Cambodia",
        "China",
        "India",
        "Indonesia",
        "Japan",
        "North Korea",
        "South Korea",
        "Laos",
        "Malaysia",
        "Mongolia",
        "Myanmar",
        "Nepal",
        "New Zealand",
        "Pakistan",
        "Philippines",
        "Russia",
        "Singapore",
        "Sri Lanka",
        "Taiwan",
        "Thailand",
        "United States",
        "Vietnam",
        "Papua New Guinea",
    ]

    pg_connection = op.get_bind()
    for country in countries:
        pg_connection.execute(f"""insert into country (id, name, created_at)
                                  values ('{uuid4()}', '{country}', '{datetime.utcnow()}')""")


def downgrade() -> None:
    pg_connection = op.get_bind()
    pg_connection.execute("truncate table country cascade")
