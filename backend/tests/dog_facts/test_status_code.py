import random

from fastapi.testclient import TestClient

from app.main import app


test_client = TestClient(app)


def test_dog_facts_return_200():
    """Ensure route returns a 200 status code"""
    response = test_client.get("/dogfacts")

    assert response.status_code == 200


def test_dog_facts_default_limit():
    """Verify that 10 results are returned, but default"""
    response = test_client.get("/dogfacts")

    assert len(response.json()["Dog facts"]) == 10


def test_dog_facts_provided_limit():
    """Ensure the route returns the given number of results"""
    random_limit = random.randrange(1, 20)
    response = test_client.get("/dogfacts", params={"facts_limit": random_limit})

    assert len(response.json()["Dog facts"]) == random_limit
