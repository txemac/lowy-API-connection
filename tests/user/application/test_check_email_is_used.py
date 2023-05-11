import pytest
from fastapi import HTTPException
from pydantic import EmailStr
from sqlmodel import Session
from starlette import status

from src import messages
from src.user.application.check_email_is_used import check_email_is_used
from src.user.domain.user import User
from src.user.domain.user_repository import UserRepository


def test_check_email_is_used_ok(
        db_sql: Session,
        user_repository: UserRepository,
) -> None:
    assert check_email_is_used(
        email=EmailStr("new_email@email.com"),
        db_sql=db_sql,
        user_repository=user_repository) is None


def test_check_email_is_used_raise(
        new_user: User,
        db_sql: Session,
        user_repository: UserRepository,
) -> None:
    with pytest.raises(HTTPException) as exception:
        check_email_is_used(email=new_user.email, db_sql=db_sql, user_repository=user_repository)
    assert exception.value.status_code == status.HTTP_409_CONFLICT
    assert exception.value.detail == messages.USER_ALREADY_EXISTS
