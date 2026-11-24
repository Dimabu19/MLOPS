from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_valid_prediction():
    response = client.post("/predict", json={"message": "Meeting at five"})
    assert response.status_code == 200
    assert "label" in response.json()
    assert response.json()["label"] in {"TODO"}, "Complete the allowed-label assertion"


def test_invalid_input():
    invalid_payloads = [
        {},
        {"message": ""},
        {"message": "   "},
    ]
    for payload in invalid_payloads:
        response = client.post("/predict", json=payload)
        assert response.status_code == 422, payload
