from typing import List
from typing import Optional

from pydantic import UUID4
from sqlmodel import Session

from src.country.domain.country import Country
from src.country.domain.country_repository import CountryRepository


class SQLModelCountryRepository(CountryRepository):

    @staticmethod
    def count(
            db_sql: Session,
    ) -> int:
        result = db_sql.query(Country).count()
        return result

    @staticmethod
    def get_by_id(
            db_sql: Session,
            country_id: UUID4,
    ) -> Optional[Country]:
        return db_sql.get(Country, country_id)

    @staticmethod
    def get_by_name(
            db_sql: Session,
            name: str,
    ) -> Optional[Country]:
        return db_sql.query(Country).where(Country.name == name).first()

    @staticmethod
    def get_all(
            db_sql: Session,
    ) -> List[Country]:
        return db_sql.query(Country).all()
