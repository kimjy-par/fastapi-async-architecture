import asyncio
import pytest
from app.models.user import User
from app.main import app
from httpx import AsyncClient, ASGITransport

@pytest.mark.asyncio(loop_scope="session")
async def test_get_user_by_id():
    # user = User(
    #    username="test_user1",
    #    email="test_user1@test.com",
    #    is_activate=True
    # )

    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://localhosts"
    ) as client:
        
        resp = await client.get("/v1/posts/5")

        print(resp.status_code)
        