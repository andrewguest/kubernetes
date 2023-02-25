from fastapi.testclient import TestClient

from app.main import app


test_client = TestClient(app)


def test_docs_return_200():
    response = test_client.get("/docs")

    assert response.status_code == 200
