import json
import pytest

from app.app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_home(client):
    response = client.get("/")

    assert response.status_code == 200

    data = response.get_json()

    assert data["application"] == "Python Flask Demo"


def test_health(client):
    response = client.get("/health")

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "Healthy"


def test_add(client):
    response = client.get("/add/10/20")

    assert response.status_code == 200

    data = response.get_json()

    assert data["result"] == 30