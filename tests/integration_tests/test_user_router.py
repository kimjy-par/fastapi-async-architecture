import asyncio
import pytest
from app.models.user import User
from app.main import app
from tests.test_utils import create_user


@pytest.mark.asyncio(loop_scope="session")
async def test_get_users(client):
    user = User(username="test_user", email="test_user@test.com", is_activate=True)

    resp = await client.get("/v1/users")
    results = resp.json()

    items = results["results"]
    total_count = results["total_count"]
    assert resp.status_code == 200
    assert total_count == 3
    assert items[0]["username"] == "kimjy1"
    assert items[1]["username"] == "kimjy2"
    assert items[2]["username"] == "kimjy3"


@pytest.mark.asyncio(loop_scope="session")
async def test_get_user_by_id(client):

    user = User(username="test_user1", email="test_user1@test.com", is_activate=True)
    user = await create_user(user)

    resp = await client.get(f"/v1/users/{user.id}")

    user_from_resp = resp.json()
    assert resp.status_code == 200
    assert user_from_resp["id"] == user.id
