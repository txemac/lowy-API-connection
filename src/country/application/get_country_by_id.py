from fastapi import Depends
from fastapi import HTTPException
from pydantic import UUID4
from sqlmodel import Session
from starlette import status

from src import messages
from src.country.domain.country import Country
from src.country.domain.country_repository import CountryRepository
from src.database import db_sql_session
from src.depends import get_country_repository


def get_country_by_id(
        country_id: UUID4,
        db_sql: Session = Depends(db_sql_session),
        country_repository: CountryRepository = Depends(get_country_repository),
) -> Country:
    """
    Get a country.

    :param country_id: ID of the Country
    :param db_sql: database SQL session
    :param country_repository: country service
    :raise: HTTPException country not found
    :return: country
    """
    country_db = country_repository.get_by_id(db_sql, country_id=country_id)
    if not country_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=messages.COUNTRY_NOT_FOUND)
    return country_db
