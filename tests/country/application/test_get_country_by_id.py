from uuid import uuid4

import pytest
from fastapi import HTTPException
from sqlmodel import Session
from starlette import status

from src import messages
from src.country.application.get_country_by_id import get_country_by_id
from src.country.domain.country import Country
from src.country.domain.country_repository import CountryRepository


def test_get_country_by_id_ok(
        country_australia: Country,
        db_sql: Session,
        country_repository: CountryRepository,
) -> None:
    assert get_country_by_id(
        country_id=country_australia.id,
        db_sql=db_sql,
        country_repository=country_repository) == country_australia


def test_get_country_by_id_non_exists(
        db_sql: Session,
        country_repository: CountryRepository,
) -> None:
    with pytest.raises(HTTPException) as exception:
        get_country_by_id(country_id=uuid4(), db_sql=db_sql, country_repository=country_repository)
    assert exception.value.status_code == status.HTTP_404_NOT_FOUND
    assert exception.value.detail == messages.COUNTRY_NOT_FOUND
