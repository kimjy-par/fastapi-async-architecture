import pytest

from starlette.testclient import TestClient
from app.main import app


@pytest.fixture
def client():
    client = TestClient(app)
    yield client
