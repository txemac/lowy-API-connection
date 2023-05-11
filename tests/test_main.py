from starlette import status
from starlette.testclient import TestClient

from src.messages import API_TITLE
from src.settings import API_VERSION
from tests.utils import assert_dicts


def test_health(
        client: TestClient,
) -> None:
    response = client.get(
        url="/health",
    )
    assert response.status_code == status.HTTP_200_OK
    expected = dict(
        title=API_TITLE,
        status="Working OK!",
        version=API_VERSION,
    )
    assert_dicts(original=response.json(), expected=expected)
