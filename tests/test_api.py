from fastapi.textclient import TestClient
from backend.app import app

client = TestClient(app)

def test_root():
    res = client.get("/")
    assert res.status_code == 200