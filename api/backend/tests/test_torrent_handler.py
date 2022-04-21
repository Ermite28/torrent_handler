from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_new_torrent():
    response = client.post("/new_torrent", json={"foo":"bar"})
    assert response.status_code == 200