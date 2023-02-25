from socket import gethostname

from fastapi.testclient import TestClient

from app.main import app


test_client = TestClient(app)


def test_healthcheck_returns_200():
    response = test_client.get("/healthcheck")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy", "hostname": gethostname()}
