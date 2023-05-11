from typing import List

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Response
from sqlmodel import Session
from starlette import status

from src import messages
from src.country.application.get_country_by_id import get_country_by_id
from src.country.domain.country import Country
from src.country.domain.country import CountryWithLowyInfo
from src.country.infrastructure.services.lowy_country_service import get_info_countries
from src.database import db_sql_session
from src.depends import get_user_repository
from src.user.application.check_email_is_used import check_email_is_used
from src.user.application.get_user_by_id import get_user_by_id
from src.user.domain.user import User
from src.user.domain.user import UserCreate
from src.user.domain.user import UserID
from src.user.domain.user import UserRead
from src.user.domain.user_repository import UserRepository

users_router = APIRouter()


@users_router.post(
    path="",
    name="Create",
    description="Create a new user.",
    status_code=status.HTTP_201_CREATED,
    response_model=UserID,
    responses={
        400: {"description": messages.USER_CREATE_ERROR},
        409: {"description": messages.USER_ALREADY_EXISTS},
    },
)
def create(
        payload: UserCreate,
        db_sql: Session = Depends(db_sql_session),
        user_repository: UserRepository = Depends(get_user_repository),
) -> UserID:
    check_email_is_used(db_sql=db_sql, user_repository=user_repository, email=payload.email)

    new_user = user_repository.create(db_sql, new_user=payload)

    if not new_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=messages.USER_CREATE_ERROR)

    return UserID(id=new_user.id)


@users_router.get(
    path="/{user_id}",
    name="Get user",
    description="Get full info about a user.",
    status_code=status.HTTP_200_OK,
    response_model=UserRead,
    responses={
        404: {"description": messages.USER_NOT_FOUND},
    },
)
def get_one(
        db_sql: Session = Depends(db_sql_session),
        user: User = Depends(get_user_by_id),
) -> UserRead:
    return user


@users_router.post(
    path="/{user_id}/add/{country_id}",
    name="Add country",
    description="Add country to user's list subscribed countries.",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        404: {"description": messages.USER_NOT_FOUND},
    },
)
def add_country(
        db_sql: Session = Depends(db_sql_session),
        user: User = Depends(get_user_by_id),
        country: Country = Depends(get_country_by_id),
        user_repository: UserRepository = Depends(get_user_repository),
) -> Response:
    user_repository.add_country(db_sql, user=user, country=country)

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@users_router.post(
    path="/{user_id}/remove/{country_id}",
    name="Remove country",
    description="Remove country to user's list subscribed countries.",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        404: {"description": messages.USER_NOT_FOUND},
    },
)
def remove_country(
        db_sql: Session = Depends(db_sql_session),
        user: User = Depends(get_user_by_id),
        country: Country = Depends(get_country_by_id),
        user_repository: UserRepository = Depends(get_user_repository),
) -> Response:
    user_repository.remove_country(db_sql, user=user, country=country)

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@users_router.get(
    path="/{user_id}/countries",
    name="Get user's countries",
    description="Get full info about countries user have subscribed to.",
    status_code=status.HTTP_200_OK,
    response_model=List[CountryWithLowyInfo],
    responses={
        404: {"description": messages.USER_NOT_FOUND},
    },
)
def get_countries(
        db_sql: Session = Depends(db_sql_session),
        user: User = Depends(get_user_by_id),
) -> List[CountryWithLowyInfo]:
    lowy_info = get_info_countries()
    return [CountryWithLowyInfo(**country.dict(), **lowy_info[country.name]) for country in user.countries]
