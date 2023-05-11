from typing import Dict

import pytest
from fastapi import HTTPException
from starlette import status

from src import messages
from src.country.infrastructure.services.lowy_country_service import __get_powers_from_country
from src.country.infrastructure.services.lowy_country_service import __get_scores_from_country
from src.country.infrastructure.services.lowy_country_service import get_info_countries


def test_get_info_countries_error(
        mock_read_lowy_url,
) -> None:
    mock_read_lowy_url.side_effect = HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                                                   detail=messages.EXTERNAL_SERVICE_ERROR)
    with pytest.raises(HTTPException) as exception:
        get_info_countries()
    assert exception.value.status_code == status.HTTP_503_SERVICE_UNAVAILABLE
    assert exception.value.detail == messages.EXTERNAL_SERVICE_ERROR


def test_get_powers_from_country(
        file_lowy_countries_url: Dict,
) -> None:
    expected = {
        2019: 63.126000000000005,
        2020: 68.729,
        2021: 62.54600000000001,
        2023: 64.02000000000001,
    }
    assert __get_powers_from_country(country=file_lowy_countries_url["countries"][0]) == expected


def test_get_scores_from_country(
        file_lowy_countries_url: Dict,
) -> None:
    expected = {
        2019: 31.332,
        2020: 32.44472,
        2021: 30.8169,
        2023: 30.93,
    }
    assert __get_scores_from_country(country=file_lowy_countries_url["countries"][0]) == expected
