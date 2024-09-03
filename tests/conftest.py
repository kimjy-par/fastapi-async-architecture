import os
import pytest
import pytest_asyncio
from app.main import app
from httpx import AsyncClient, ASGITransport
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy import orm
from app.core.config import configs
from app.core.database import Database
from tests.test_utils import insert_data, delete_all_records

if configs.ENV != "test":
    msg = f"ENV is not test, it is {os.getenv('ENV')}"
    pytest.exit(msg)


async def setup():
    await delete_all_records()
    await insert_data()


async def teardown():
    await delete_all_records()


@pytest_asyncio.fixture(loop_scope="session")
async def session():
    engine = create_async_engine(configs.DB_URL)
    async with AsyncSession(engine) as session:
        yield session
        await session.rollback()


@pytest_asyncio.fixture(loop_scope="session")
async def client():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://localhost"
    ) as client:
        await setup()
        yield client
        await teardown()


@pytest_asyncio.fixture(loop_scope="session")
async def database():
    database = Database(configs.DB_URL)
    yield database
    await teardown()
