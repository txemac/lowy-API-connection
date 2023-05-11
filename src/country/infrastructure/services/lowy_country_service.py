"""
External connection at Lowy Institute
https://power.lowyinstitute.org

Unofficial API documentation: https://github.com/0x0is1/lowy-index-api-docs

API BASE URL: https://power.lowyinstitute.org

API Reference

GET /world.json	- World topology data
GET /countries.json	- Get List of all countries with power and various score including Country's slug
GET {country_slug}.json	- Get score, influence, lat-long and other additional data.
GET /data/{Year}.json - Get score, rank and country code of Countries by Year (2018+)
GET /network-power.json - Get Economic, Cultural, Defence and Diplomatic networks of countries

"""
import json
from typing import Dict
from urllib.request import urlopen

from fastapi import HTTPException
from starlette import status

from src import messages
from src.settings import LOWY_BASE_URL


# endpoint
def __read_lowy_url() -> Dict:
    """
    Get JSON from lowy URL.
    example:
    {
        'countries': [
            {
                'id': 'AU',
                'name': 'Australia',
                'slug': 'australia',
                'href': '/countries/australia/',
                'power': [
                    {
                        'c': 'AU',
                        'year': 2023,
                        'gap': 7.03,
                        'expected': 23.9,
                        'resources': 22.32,
                        'influence': 41.45,
                        'trend': 0.25,
                        'change': 0,
                        'rank': 2
                    },
                    {
                        'c': 'AU',
                        'year': 2021,
                        'rank': 2,
                        'gap': 6.8,
                        'expected': 24,
                        'resources': 22.8,
                        'influence': 40.6,
                        'trend': -0.854,
                        'change': 0
                    },
                ],
                'latitude': -25,
                'scores': [
                    {
                        'year': 2023,
                        'score': 30.93,
                        'rank': 6,
                        'trend': 0.1132,
                        'pretrend': 0.0037,
                        'm': 0,
                        'c': 'AU'
                    },
                    {
                        'year': 2019,
                        'score': 31.332,
                        'rank': 7,
                        'trend': -0.181763,
                        'pretrend': -0.005768,
                        'm': 0,
                        'c': 'AU'
                    },
                ],
            },
        ]
    }

    :return Dict: countries info
    """
    try:
        with urlopen(f"{LOWY_BASE_URL}/countries.json") as url:
            return json.load(url)
    except Exception:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail=messages.EXTERNAL_SERVICE_ERROR)


def __get_powers_from_country(
        country: Dict,
) -> Dict[str, float]:
    result = dict()
    for power in country["power"]:
        result[power["year"]] = sum([power.get("trend") or 0, power.get("resources") or 0, power.get("influence") or 0])
    return result


def __get_scores_from_country(
        country: Dict,
) -> Dict[str, float]:
    result = dict()
    for score in country["scores"]:
        result[score["year"]] = score["score"]
    return result


def get_info_countries() -> Dict:
    info_from_json = __read_lowy_url()

    lowy_info = dict()
    for country in info_from_json.get("countries"):
        lowy_info[country.get("name")] = dict(
            powers=__get_powers_from_country(country=country),
            scores=__get_scores_from_country(country=country),
        )

    return lowy_info
