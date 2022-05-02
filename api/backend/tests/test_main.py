from fastapi.testclient import TestClient
from main import app
from core.config import get_settings, Settings

client = TestClient(app)

def get_settings_override():
    return Settings(TMDB_KEY='test')

app.dependency_overrides[get_settings] = get_settings_override

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "hello"}
