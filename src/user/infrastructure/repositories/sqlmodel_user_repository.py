from typing import Optional

from pydantic import EmailStr
from pydantic import UUID4
from sqlmodel import Session

from src.country.domain.country import Country
from src.user.domain.user import User
from src.user.domain.user import UserCreate
from src.user.domain.user_repository import UserRepository


class SQLModelUserRepository(UserRepository):

    @staticmethod
    def count(
            db_sql: Session,
    ) -> int:
        result = db_sql.query(User).count()
        return result

    @staticmethod
    def create(
            db_sql: Session,
            new_user: UserCreate,
    ) -> User:
        user = User.from_orm(new_user)
        db_sql.add(user)
        db_sql.commit()
        db_sql.refresh(user)
        return user

    @staticmethod
    def get_by_id(
            db_sql: Session,
            user_id: UUID4,
    ) -> Optional[User]:
        return db_sql.get(User, user_id)

    @staticmethod
    def get_by_email(
            db_sql: Session,
            email: EmailStr,
    ) -> Optional[User]:
        return db_sql.query(User).where(User.email == email).first()

    @staticmethod
    def add_country(
            db_sql: Session,
            user: User,
            country: Country,
    ) -> None:
        if country not in user.countries:
            user.countries.append(country)
            db_sql.add(user)
            db_sql.commit()
            db_sql.refresh(user)

    @staticmethod
    def remove_country(
            db_sql: Session,
            user: User,
            country: Country,
    ) -> None:
        if country in user.countries:
            user.countries.remove(country)
            db_sql.add(user)
            db_sql.commit()
            db_sql.refresh(user)
