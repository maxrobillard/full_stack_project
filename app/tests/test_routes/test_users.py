import json


def test_create_user(client):
    data = {"email": "testuser@fullstack.com", "password": "testing"}
    response = client.post("/users/", json.dumps(data))
    assert response.status_code == 200
    assert response.json()["email"] == "testuser@fullstack.com"
    assert response.json()["is_active"] == True
