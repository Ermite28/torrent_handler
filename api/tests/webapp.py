import pytest
from app import app


@pytest.fixture
def client():
    print("ok")
    client = app.test_client()

    return client
