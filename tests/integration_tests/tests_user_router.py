def test_get_users(client):
    resp = client.get("/v1/users")
    assert resp.status_code == 200
    assert resp.json() == []