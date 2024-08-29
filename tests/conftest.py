import asyncio
import pytest

from contextlib import asynccontextmanager
from starlette.testclient import TestClient
from app.main import app
from httpx import AsyncClient, ASGITransport
from test_utils import create_users, delete_all_records
from pytest_asyncio import is_async_test

# def setup():
#    loop = asyncio.get_event_loop()
#    loop.run_until_complete(delete_all_records())
#    loop.run_until_complete(create_users())

# def teardown():
# loop = asyncio.get_event_loop()
# loop.run_until_complete(delete_all_records())

