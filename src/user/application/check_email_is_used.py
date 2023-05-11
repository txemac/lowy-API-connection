from fastapi import Depends
from fastapi import HTTPException
from pydantic import EmailStr
from sqlalchemy.orm import Session
from starlette import status

from src import messages
from src.database import db_sql_session
from src.depends import get_user_repository
from src.user.domain.user_repository import UserRepository


def check_email_is_used(
        email: EmailStr,
        db_sql: Session = Depends(db_sql_session),
        user_repository: UserRepository = Depends(get_user_repository),
) -> None:
    """
    Check if the email already in use at system.

    :param email: canonical email
    :param db_sql: database SQL session
    :param user_repository: user service
    :raise: HTTPException email already exists
    """
    if user_repository.get_by_email(db_sql, email=email):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=messages.USER_ALREADY_EXISTS)
