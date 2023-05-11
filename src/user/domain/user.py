from datetime import datetime
from typing import List
from uuid import uuid4

from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import UUID4
from pydantic.types import constr
from sqlmodel import Field
from sqlmodel import Relationship
from sqlmodel import SQLModel

from src.country.domain.country import Country
from src.user.domain.user_country_link import UserCountryLink


class UserCreate(SQLModel):
    email: EmailStr = Field(unique=True, index=True)
    name: constr(min_length=1)

    class Config:
        schema_extra = dict(
            example=dict(
                email="txema@email.com",
                name="Txema",
            )
        )


class UserID(BaseModel):
    id: UUID4 = Field(default_factory=uuid4, primary_key=True, nullable=False)

    class Config:
        schema_extra = dict(
            example=dict(
                id="eb75b926-8b44-4fae-a744-b3b3f96d98cd",
            )
        )


class User(UserCreate, UserID, table=True):
    __tablename__ = "user"

    countries: List[Country] = Relationship(back_populates="users", link_model=UserCountryLink)
    created_at: datetime = datetime.utcnow()

    def __repr__(self):
        return self.email

    class Config:
        orm_mode = True
        read_with_orm_mode = True


class UserRead(UserID, UserCreate):
    countries: List[Country] = []
    created_at: datetime

    class Config:
        schema_extra = dict(
            example=dict(
                **UserID.Config.schema_extra.get("example"),
                **UserCreate.Config.schema_extra.get("example"),
                created_at="2022-10-20 12:34:56",
                countries=[Country.Config.schema_extra.get("example")]
            )
        )
