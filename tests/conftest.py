import asyncio
import pytest
import pytest_asyncio
from contextlib import asynccontextmanager
from starlette.testclient import TestClient
from app.main import app
from httpx import AsyncClient, ASGITransport
from tests.test_utils import create_users, delete_all_records
from pytest_asyncio import is_async_test


async def setup():
    await create_users()


async def teardown():
    await delete_all_records()


@pytest_asyncio.fixture
async def client():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://localhost"
    ) as client:
        await create_users()
        yield client
        await delete_all_records()
