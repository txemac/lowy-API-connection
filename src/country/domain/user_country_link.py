from datetime import datetime

from pydantic import UUID4
from sqlmodel import Field
from sqlmodel import SQLModel


class UserCountryLink(SQLModel, table=True):
    __tablename__ = "user_country_link"

    user_id: UUID4 = Field(foreign_key="user.id", primary_key=True)
    country_id: UUID4 = Field(foreign_key="country.id", primary_key=True)
    created_at: datetime = datetime.utcnow()
