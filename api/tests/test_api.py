from .webapp import client


def test_index():
    assert "Index" == client.get("/")
