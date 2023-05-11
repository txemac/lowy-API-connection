from abc import ABC
from abc import abstractmethod
from typing import List
from typing import Optional

from pydantic import UUID4
from sqlmodel import Session

from src.country.domain.country import Country


class CountryRepository(ABC):

    @staticmethod
    @abstractmethod
    def count(
            db_sql: Session,
    ) -> int:
        """
        Count the number of element in the country table.

        :param db_sql: session of the SQL database
        :return: number of countries
        """
        pass

    @staticmethod
    @abstractmethod
    def get_by_id(
            db_sql: Session,
            country_id: UUID4,
    ) -> Optional[Country]:
        """
        Searches for a persisted country by ID and returns it if it exists.

        :param db_sql: session of the SQL database
        :param country_id: country's ID
        :return: country if found, None otherwise
        """
        pass

    @staticmethod
    @abstractmethod
    def get_by_name(
            db_sql: Session,
            name: str,
    ) -> Optional[Country]:
        """
        Searches for a persisted country by name "unique" and returns it if it exists.

        :param db_sql: session of the SQL database
        :param name: name of the country
        :return: country if found, None otherwise
        """
        pass

    @staticmethod
    @abstractmethod
    def get_all(
            db_sql: Session,
    ) -> List[Country]:
        """
        Get info about all countries at database.

        :param db_sql: session of the SQL database
        :return: list of countries
        """
        pass
