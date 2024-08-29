import asyncio
import pytest
from app.models.user import User
from app.main import app
from httpx import AsyncClient, ASGITransport


@pytest.mark.asyncio(loop_scope="session")
async def test_get_users():
    user = User(username="test_user", email="test_user@test.com", is_activate=True)

    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://localhost"
    ) as client:
        print(await client.get("/v1/users"))
    # resp = sync_client.get("/v1/users")
    # results = resp.json()

    # items = results["results"]
    # total_count = results["total_count"]
    # print(resp)
    # assert resp.status_code == 200
    # assert total_count == 3
    # assert items[0]["username"] == "kimjy1"
    # assert items[1]["username"] == "kimjy2"
    # assert items[2]["username"] == "kimjy3"

"""
@pytest.mark.asyncio
async def test_get_user_by_id():
    # user = User(
    #    username="test_user1",
    #    email="test_user1@test.com",
    #    is_activate=True
    # )

    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://localhost"
    ) as client:
        print(await client.get("/v1/users/574"))
    # user = user_add(user)
    # user_id = user.id
    # print("!!!!!userid", user_id, )
    # resp = sync_client.get(f'/v1/users/577')
    # print(resp)
    # resp = client.get(f"/v1/users")
    # result = resp.json()

    # assert resp.status_code == 200
    # assert result["id"] == first_user_id
    ...


def user_add(user):
    loop = asyncio.get_event_loop()
    user = loop.run_until_complete(create_user(user))
    return user
"""