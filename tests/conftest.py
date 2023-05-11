from copy import deepcopy

import pytest
from alembic.command import downgrade
from alembic.command import upgrade
from alembic.config import Config
from sqlalchemy_utils import create_database
from sqlalchemy_utils import database_exists
from sqlmodel import Session
from sqlmodel import create_engine
from starlette.config import environ
from starlette.testclient import TestClient

from src.country.domain.country import Country
from src.country.domain.country_repository import CountryRepository
from src.country.infrastructure.repositories.sqlmodel_country_repository import SQLModelCountryRepository
from src.database import db_sql_session
from src.main import api
from src.settings import DATABASE_URL
from src.user.domain.user import User
from src.user.domain.user import UserCreate
from src.user.domain.user_repository import UserRepository
from src.user.infrastructure.repositories.sqlmodel_user_repository import SQLModelUserRepository

environ["TESTING"] = "True"


@pytest.fixture
def client(
        db_sql: Session,
) -> TestClient:
    def _get_test_db():
        try:
            yield db_sql
        finally:
            pass

    api.dependency_overrides[db_sql_session] = _get_test_db
    with TestClient(api) as client:
        yield client


@pytest.fixture(scope="session")
def db_engine():
    engine = create_engine(DATABASE_URL, pool_pre_ping=True)
    if not database_exists(engine.url):
        create_database(engine.url)
    return engine


@pytest.fixture(scope="session")
def db_migrations(db_engine) -> None:
    config = Config("alembic.ini")
    upgrade(config, "head")
    yield
    downgrade(config, "base")


@pytest.fixture
def db_sql(db_engine, db_migrations) -> Session:
    connection = db_engine.connect()
    transaction = connection.begin()
    session = Session(bind=connection)

    yield session

    session.close()
    transaction.rollback()
    connection.close()


@pytest.fixture
def user_repository() -> UserRepository:
    return SQLModelUserRepository()


@pytest.fixture
def country_repository() -> CountryRepository:
    return SQLModelCountryRepository()


@pytest.fixture
def new_user_data(
        country_cambodia: Country,
        country_vietnam: Country,
) -> dict:
    return deepcopy(UserCreate.Config.schema_extra.get("example"))


@pytest.fixture
def country_australia(
        db_sql: Session,
        country_repository: CountryRepository,
) -> Country:
    return country_repository.get_by_name(db_sql, name="Australia")


@pytest.fixture
def country_vietnam(
        db_sql: Session,
        country_repository: CountryRepository,
) -> Country:
    return country_repository.get_by_name(db_sql, name="Vietnam")


@pytest.fixture
def country_cambodia(
        db_sql: Session,
        country_repository: CountryRepository,
) -> Country:
    return country_repository.get_by_name(db_sql, name="Cambodia")


@pytest.fixture
def new_user(
        db_sql: Session,
        user_repository: UserRepository,
        new_user_data: dict,
        country_cambodia: Country,
        country_vietnam: Country,
) -> User:
    user = user_repository.create(db_sql, new_user=UserCreate(**new_user_data))
    user_repository.add_country(db_sql, user=user, country=country_cambodia)
    user_repository.add_country(db_sql, user=user, country=country_vietnam)
    return user
