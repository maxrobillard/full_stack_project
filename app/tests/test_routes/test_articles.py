import json


def test_create_article(client):
    data = {
        "title": "Covid",
        "body": "Actuellement en France",
        "date_posted": "2022-03-20"
        }
    response = client.post("/articles/create-article/", json.dumps(data))
    assert response.status_code == 200 
    assert response.json()["title"] == "Covid"
    assert response.json()["body"] == "Actuellement en France"
