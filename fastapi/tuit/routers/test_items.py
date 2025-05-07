from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_fake_items_200():
    response = client.get("/items/fake_items/one")
    assert response.status_code == 200

def test_fake_items_404():
    response = client.get("/items/fake_items/foobar")
    assert response.status_code == 404
    assert "x-error" in response.headers
