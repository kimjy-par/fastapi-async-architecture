import pytest
from app.models.user import User
from tests.test_utils import create_user


@pytest.mark.asyncio(loop_scope="session")
async def test_get_users(client):
    resp = await client.get("/v1/users")

    assert resp.status_code == 200


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

    user = User(
        username="user_for_change", email="user_for_change@test.com", is_activate=True
    )
    user = await create_user(user)

    to_be_change = {
        "username": "change_user",
        "email": "change_user@change.com",
        "is_activate": False,
    }
    resp = await client.patch(f"/v1/users/{user.id}", json=to_be_change)
    changed_from_resp = resp.json()

    assert resp.status_code == 200
    assert user.id == changed_from_resp["id"]
    assert changed_from_resp["username"] == "change_user"
    assert changed_from_resp["email"] == "change_user@change.com"
    assert changed_from_resp["is_activate"] == False


@pytest.mark.asyncio(loop_scope="session")
async def test_delete_user(client):
    user = User(
        username="user_for_delete", email="user_for_delete@test.com", is_activate=True
    )
    user = await create_user(user)

    resp = await client.delete(f"/v1/users/{user.id}")

    assert resp.status_code == 204

    resp_with_first_user_id = await client.get(f"/v1/users/{user.id}")
    assert resp_with_first_user_id.status_code == 404
