import asyncio
import pytest

from contextlib import asynccontextmanager
from starlette.testclient import TestClient
from app.main import app
from httpx import AsyncClient, ASGITransport
from test_utils import create_users, delete_all_records


# def setup():
#    loop = asyncio.get_event_loop()
#    loop.run_until_complete(delete_all_records())
#    loop.run_until_complete(create_users())

# def teardown():
# loop = asyncio.get_event_loop()
# loop.run_until_complete(delete_all_records())


@pytest.fixture(scope="session")
def event_loop():
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
    yield loop
    loop.close()

@pytest.fixture
async def client(event_loop):
    client = AsyncClient(transport=ASGITransport(app=app), base_url="http://localhost")
    print("fixture", client)
    yield client


@pytest.fixture
def sync_client(event_loop):
    client = TestClient(app=app)
    yield client
    # teardown()
