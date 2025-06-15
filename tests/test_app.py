from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health():
    assert client.get("/healthz").json() == {"status": "ok"}

def test_review():
    assert client.post("/review").json() == {"todo": True}