from fastapi import Depends
from fastapi import HTTPException
from pydantic import UUID4
from sqlmodel import Session
from starlette import status

from src import messages
from src.database import db_sql_session
from src.depends import get_user_repository
from src.user.domain.user import User
from src.user.domain.user_repository import UserRepository


def get_user_by_id(
        user_id: UUID4,
        db_sql: Session = Depends(db_sql_session),
        user_repository: UserRepository = Depends(get_user_repository),
) -> User:
    """
    Get a user.

    :param user_id: User's ID
    :param db_sql: database SQL session
    :param user_repository: user service
    :raise: HTTPException user nor found
    :return: user
    """
    user_db = user_repository.get_by_id(db_sql, user_id=user_id)
    if not user_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=messages.USER_NOT_FOUND)
    return user_db
