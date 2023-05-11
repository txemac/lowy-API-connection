from uuid import uuid4

from pydantic import UUID4
from sqlmodel import Session

from src.country.domain.country import Country
from src.country.domain.country_repository import CountryRepository
from tests.utils import assert_dicts


def test_count(
        db_sql: Session,
        country_repository: CountryRepository,
) -> None:
    assert country_repository.count(db_sql) == 26


def test_get_by_id_ok(
        db_sql: Session,
        country_repository: CountryRepository,
        country_australia: Country,
) -> None:
    result = country_repository.get_by_id(db_sql, country_id=country_australia.id)
    assert_dicts(original=result.dict(), expected=country_australia.dict())


def test_get_by_id_not_exists(
        db_sql: Session,
        country_repository: CountryRepository,
) -> None:
    assert country_repository.get_by_id(db_sql, country_id=UUID4(str(uuid4()))) is None


def test_get_by_name_ok(
        db_sql: Session,
        country_repository: CountryRepository,
        country_australia: Country,
) -> None:
    result = country_repository.get_by_name(db_sql, name=country_australia.name)
    assert_dicts(original=result.dict(), expected=country_australia.dict())


def test_get_by_name_not_exists(
        db_sql: Session,
        country_repository: CountryRepository,
) -> None:
    assert country_repository.get_by_name(db_sql, name="Spain") is None
