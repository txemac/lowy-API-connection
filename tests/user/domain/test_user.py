from typing import Any
from typing import Dict

import pytest
from pydantic import ValidationError

from src.user.domain.user import UserCreate


def test_user_create_ok(
        new_user_data: Dict,
) -> None:
    assert UserCreate(**new_user_data)


@pytest.mark.parametrize(
    "attr",
    [
        "email",
        "name",
    ]
)
def test_user_create_attr_pop(
        new_user_data: Dict,
        attr: str,
) -> None:
    new_user_data.pop(attr)
    with pytest.raises(ValidationError) as exception:
        UserCreate(**new_user_data)
    assert attr in str(exception.value)


@pytest.mark.parametrize(
    "attr",
    [
        "email",
        "name",
    ]
)
def test_user_create_attr_none(
        new_user_data: Dict,
        attr: str,
) -> None:
    new_user_data[attr] = None
    with pytest.raises(ValidationError) as exception:
        UserCreate(**new_user_data)
    assert attr in str(exception.value)


@pytest.mark.parametrize(
    "attr, value",
    [
        ("email", ""),
        ("email", "wrong_email"),
        ("name", ""),
    ]
)
def test_user_create_wrong(
        new_user_data: Dict,
        attr: str,
        value: Any,
) -> None:
    new_user_data[attr] = value
    with pytest.raises(ValidationError) as exception:
        UserCreate(**new_user_data)
    assert attr in str(exception.value)
