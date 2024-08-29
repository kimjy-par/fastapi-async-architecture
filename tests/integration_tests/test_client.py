import pytest
from app.main import app

from httpx import AsyncClient, ASGITransport


@pytest.mark.asyncio
async def test_client(sync_client):
    # async with AsyncClient(transport=ASGITransport(app=app), base_url="http://localhost") as client:
    # async with client() as client:
    print(sync_client)
    response = sync_client.get("/")

    assert response.status_code == 200
    assert response.json() == {"health": True}
