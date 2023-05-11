from uuid import uuid4

from sqlmodel import Session
from starlette import status
from starlette.testclient import TestClient

from src import messages
from src.country.domain.country import Country
from src.user.application.get_user_by_id import get_user_by_id
from src.user.domain.user import User
from src.user.domain.user_repository import UserRepository
from tests.utils import assert_dicts


def test_user_create_ok(
        client: TestClient,
) -> None:
    data = dict(
        name="Txema",
        email="txema@email.com",
        countries_ids=[],
    )
    response = client.post(
        url="/users",
        json=data,
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json().get("id") is not None


def test_user_create_email_already_exists(
        client: TestClient,
        new_user: User,
) -> None:
    data = dict(
        name="Txema",
        email=new_user.email,
        countries_ids=[],
    )
    response = client.post(
        url="/users",
        json=data,
    )
    assert response.status_code == status.HTTP_409_CONFLICT
    assert response.json().get("detail") == messages.USER_ALREADY_EXISTS


def test_user_get_one_ok(
        client: TestClient,
        new_user: User,
) -> None:
    response = client.get(
        url=f"/users/{new_user.id}",
    )
    assert response.status_code == status.HTTP_200_OK
    assert_dicts(original=response.json(), expected=new_user.dict())


def test_user_add_country_ok(
        client: TestClient,
        db_sql: Session,
        user_repository: UserRepository,
        new_user: User,
        country_australia: Country,
) -> None:
    response = client.post(
        url=f"/users/{new_user.id}/add/{country_australia.id}",
    )
    assert response.status_code == status.HTTP_204_NO_CONTENT

    user_db = get_user_by_id(user_id=new_user.id, db_sql=db_sql, user_repository=user_repository)
    assert country_australia in user_db.countries


def test_user_add_country_already_exists(
        client: TestClient,
        db_sql: Session,
        user_repository: UserRepository,
        new_user: User,
) -> None:
    response = client.post(
        url=f"/users/{new_user.id}/add/{new_user.countries[0].id}",
    )
    assert response.status_code == status.HTTP_204_NO_CONTENT

    user_db = get_user_by_id(user_id=new_user.id, db_sql=db_sql, user_repository=user_repository)
    assert new_user.countries == user_db.countries


def test_user_add_country_user_id_not_exists(
        client: TestClient,
        db_sql: Session,
        user_repository: UserRepository,
        country_australia: Country,
) -> None:
    response = client.post(
        url=f"/users/{uuid4()}/add/{country_australia.id}",
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json().get("detail") == messages.USER_NOT_FOUND


def test_user_add_country_country_id_not_exists(
        client: TestClient,
        db_sql: Session,
        user_repository: UserRepository,
        new_user: User,
) -> None:
    response = client.post(
        url=f"/users/{new_user.id}/add/{uuid4()}",
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json().get("detail") == messages.COUNTRY_NOT_FOUND


def test_user_remove_country_ok(
        client: TestClient,
        db_sql: Session,
        user_repository: UserRepository,
        new_user: User,
) -> None:
    country_to_remove = new_user.countries[0]
    response = client.post(
        url=f"/users/{new_user.id}/remove/{country_to_remove.id}",
    )
    assert response.status_code == status.HTTP_204_NO_CONTENT

    user_db = get_user_by_id(user_id=new_user.id, db_sql=db_sql, user_repository=user_repository)
    assert country_to_remove not in user_db.countries


def test_user_remove_country_not_exists(
        client: TestClient,
        db_sql: Session,
        user_repository: UserRepository,
        new_user: User,
        country_australia: Country,
) -> None:
    response = client.post(
        url=f"/users/{new_user.id}/remove/{country_australia.id}",
    )
    assert response.status_code == status.HTTP_204_NO_CONTENT

    user_db = get_user_by_id(user_id=new_user.id, db_sql=db_sql, user_repository=user_repository)
    assert new_user.countries == user_db.countries


def test_user_remove_country_user_id_not_exists(
        client: TestClient,
        db_sql: Session,
        user_repository: UserRepository,
        country_australia: Country,
) -> None:
    response = client.post(
        url=f"/users/{uuid4()}/remove/{country_australia.id}",
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json().get("detail") == messages.USER_NOT_FOUND


def test_user_remove_country_country_id_not_exists(
        client: TestClient,
        db_sql: Session,
        user_repository: UserRepository,
        new_user: User,
) -> None:
    response = client.post(
        url=f"/users/{new_user.id}/remove/{uuid4()}",
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json().get("detail") == messages.COUNTRY_NOT_FOUND
