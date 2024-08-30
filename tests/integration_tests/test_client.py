import pytest
from app.main import app

from httpx import AsyncClient, ASGITransport


@pytest.mark.asyncio(loop_scope="session")
async def test_client():
    # async with AsyncClient(transport=ASGITransport(app=app), base_url="http://localhost") as client:
    # async with client() as client:
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://localhost"
    ) as client:
        print(await client.get("/v1/users"))
    # assert response.status_code == 200
    # assert response.json() == {"health": True}
