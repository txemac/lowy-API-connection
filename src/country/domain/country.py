from datetime import datetime
from typing import Dict
from typing import List
from uuid import uuid4

from pydantic import BaseModel
from pydantic import UUID4
from pydantic import conint
from sqlmodel import Field
from sqlmodel import Relationship
from sqlmodel import SQLModel

from src.user.domain.user_country_link import UserCountryLink


class Country(SQLModel, BaseModel, table=True):
    __tablename__ = "country"

    id: UUID4 = Field(default_factory=uuid4, primary_key=True, nullable=False)
    name: str
    users: List["User"] = Relationship(back_populates="countries", link_model=UserCountryLink)  # noqa: F821
    created_at: datetime = datetime.utcnow()

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        return self.id == other.id

    class Config:
        orm_mode = True
        read_with_orm_mode = True
        schema_extra = dict(
            example=dict(
                id="eb75b926-8b44-4fae-a744-b3b3f96d98cd",
                created_at="2022-20-20 12:34:56",
                name="Australia",
            )
        )


class CountryWithLowyInfo(BaseModel):
    id: UUID4
    name: str
    created_at: datetime
    powers: Dict[conint(ge=2018), float]
    scores: Dict[conint(ge=2018), float]

    class Config:
        orm_mode = True
        read_with_orm_mode = True
        schema_extra = dict(
            example=dict(
                id="eb75b926-8b44-4fae-a744-b3b3f96d98cd",
                created_at="2022-20-20 12:34:56",
                name="Australia",
                powers={
                    2018: 20.02,
                    2021: 19.81,
                },
                scores={
                    2018: 20.02,
                    2021: 19.81,
                },
            )
        )
