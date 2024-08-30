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


@pytest.mark.asyncio(loop_scope="session")
async def test_create_user(client):

    json_body = {
        "username": "test_user",
        "email": "test_post_user@test.com",
        "is_activate": True,
    }
    resp = await client.post("/v1/users", json=json_body)
    user_from_resp = resp.json()

    assert resp.status_code == 201
    assert user_from_resp["username"] == "test_user"
    assert user_from_resp["email"] == "test_post_user@test.com"
    assert user_from_resp["is_activate"] == True


@pytest.mark.asyncio(loop_scope="session")
async def test_update_user(client):

    get_users_resp = await client.get("/v1/users")
    get_resp_json = get_users_resp.json()
    first_user = get_resp_json["results"][0]

    first_user_id = first_user["id"]

    to_be_change = {
        "username": "change_user",
        "email": "change_user@change.com",
        "is_activate": False,
    }
    resp = await client.patch(f"/v1/users/{first_user_id}", json=to_be_change)
    changed_from_resp = resp.json()

    assert resp.status_code == 200
    assert first_user_id == changed_from_resp["id"]
    assert changed_from_resp["username"] == "change_user"
    assert changed_from_resp["email"] == "change_user@change.com"
    assert changed_from_resp["is_activate"] == False

@pytest.mark.asyncio(loop_scope="session")
async def test_delete_user(client):
    get_users_resp = await client.get("/v1/users")
    get_resp_json = get_users_resp.json()
    first_user = get_resp_json["results"][0]

    first_user_id = first_user["id"] 

    resp = await client.delete(f"/v1/users/{first_user_id}")

    assert resp.status_code == 204

    resp_with_first_user_id = await client.get(f"/v1/users/{first_user_id}")
    assert resp_with_first_user_id.status_code == 404