from typing import List

from fastapi import APIRouter
from fastapi import Depends
from sqlmodel import Session
from starlette import status

from src.country.domain.country import Country
from src.country.domain.country_repository import CountryRepository
from src.database import db_sql_session
from src.depends import get_country_repository

countries_router = APIRouter()


@countries_router.get(
    path="",
    name="Get countries",
    description="Get list of countries.",
    status_code=status.HTTP_200_OK,
    response_model=List[Country],
)
def get_list(
        db_sql: Session = Depends(db_sql_session),
        country_repository: CountryRepository = Depends(get_country_repository),
) -> List[Country]:
    return country_repository.get_all(db_sql)
