import pytest


@pytest.mark.asyncio(loop_scope="session")
async def test_client(client):
    resp = await client.get("/")
    assert resp.status_code == 200
    assert resp.json() == {"health": True}
