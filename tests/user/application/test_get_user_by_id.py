from uuid import uuid4

import pytest
from fastapi import HTTPException
from sqlmodel import Session
from starlette import status

from src import messages
from src.user.application.get_user_by_id import get_user_by_id
from src.user.domain.user import User
from src.user.domain.user_repository import UserRepository


def test_get_user_by_id_ok(
        new_user: User,
        db_sql: Session,
        user_repository: UserRepository,
) -> None:
    assert get_user_by_id(user_id=new_user.id, db_sql=db_sql, user_repository=user_repository) == new_user


def test_get_user_by_id_non_exists(
        db_sql: Session,
        user_repository: UserRepository,
) -> None:
    with pytest.raises(HTTPException) as exception:
        get_user_by_id(user_id=uuid4(), db_sql=db_sql, user_repository=user_repository)
    assert exception.value.status_code == status.HTTP_404_NOT_FOUND
    assert exception.value.detail == messages.USER_NOT_FOUND
