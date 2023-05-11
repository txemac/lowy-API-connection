from src.country.domain.country_repository import CountryRepository
from src.country.infrastructure.repositories.sqlmodel_country_repository import SQLModelCountryRepository
from src.user.domain.user_repository import UserRepository
from src.user.infrastructure.repositories.sqlmodel_user_repository import SQLModelUserRepository


def get_user_repository() -> UserRepository:
    return SQLModelUserRepository()


def get_country_repository() -> CountryRepository:
    return SQLModelCountryRepository()
