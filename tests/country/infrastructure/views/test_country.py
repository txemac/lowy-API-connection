from starlette import status
from starlette.testclient import TestClient


def test_country_get_list(
        client: TestClient,
) -> None:
    response = client.get(
        url="/countries",
    )
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 26
