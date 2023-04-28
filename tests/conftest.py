import pytest
from starlette.config import environ
from starlette.testclient import TestClient

from src.main import api

environ["TESTING"] = "True"


@pytest.fixture
def client() -> TestClient:
    with TestClient(api) as client:
        yield client
