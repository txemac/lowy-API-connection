from typing import Dict
from uuid import uuid4

from pydantic import EmailStr
from pydantic import UUID4
from sqlmodel import Session

from src.country.domain.country import Country
from src.country.domain.country_repository import CountryRepository
from src.user.domain.user import User
from src.user.domain.user import UserCreate
from src.user.domain.user_repository import UserRepository
from tests.utils import assert_dicts


def test_count_0(
        db_sql: Session,
        user_repository: UserRepository,
) -> None:
    assert user_repository.count(db_sql) == 0


def test_count_1(
        db_sql: Session,
        user_repository: UserRepository,
        new_user: User,
) -> None:
    assert user_repository.count(db_sql) == 1


def test_create_ok(
        db_sql: Session,
        user_repository: UserRepository,
        country_repository: CountryRepository,
        new_user_data: Dict,
) -> None:
    count_user_1 = user_repository.count(db_sql)
    user = user_repository.create(db_sql, new_user=UserCreate(**new_user_data))
    count_user_2 = user_repository.count(db_sql)

    assert count_user_1 + 1 == count_user_2

    assert user_repository.get_by_id(db_sql, user_id=user.id) == user


def test_get_by_id_ok(
        db_sql: Session,
        user_repository: UserRepository,
        new_user: User,
) -> None:
    result = user_repository.get_by_id(db_sql, user_id=new_user.id)
    assert_dicts(original=result.dict(), expected=new_user.dict())


def test_get_by_id_not_exists(
        db_sql: Session,
        user_repository: UserRepository,
) -> None:
    assert user_repository.get_by_id(db_sql, user_id=UUID4(str(uuid4()))) is None


def test_get_by_email_ok(
        db_sql: Session,
        user_repository: UserRepository,
        new_user: User,
) -> None:
    result = user_repository.get_by_email(db_sql, email=new_user.email)
    assert_dicts(original=result.dict(), expected=new_user.dict())


def test_get_by_email_not_exists(
        db_sql: Session,
        user_repository: UserRepository,
) -> None:
    assert user_repository.get_by_email(db_sql, email=EmailStr("wrong@email.com")) is None


def test_add_country_ok(
        db_sql: Session,
        new_user: User,
        country_australia: Country,
        user_repository: UserRepository,
) -> None:
    assert len(new_user.countries) == 2
    user_repository.add_country(db_sql, user=new_user, country=country_australia)
    assert len(new_user.countries) == 3

    user_db = user_repository.get_by_id(db_sql, user_id=new_user.id)
    assert country_australia in user_db.countries


def test_add_country_already_in_list(
        db_sql: Session,
        new_user: User,
        user_repository: UserRepository,
) -> None:
    assert len(new_user.countries) == 2
    user_repository.add_country(db_sql, user=new_user, country=new_user.countries[0])
    assert len(new_user.countries) == 2


def test_remove_country_ok(
        db_sql: Session,
        new_user: User,
        user_repository: UserRepository,
) -> None:
    assert len(new_user.countries) == 2
    country_to_remove = new_user.countries[0]
    user_repository.remove_country(db_sql, user=new_user, country=country_to_remove)
    assert len(new_user.countries) == 1

    user_db = user_repository.get_by_id(db_sql, user_id=new_user.id)
    assert country_to_remove not in user_db.countries


def test_remove_country_not_in_list(
        db_sql: Session,
        new_user: User,
        user_repository: UserRepository,
        country_australia: Country,
) -> None:
    assert len(new_user.countries) == 2
    user_repository.remove_country(db_sql, user=new_user, country=country_australia)
    assert len(new_user.countries) == 2
