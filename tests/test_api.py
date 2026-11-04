#test api outside readme md
import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture
def client():
    with TestClient(app) as test_client:
        yield test_client

def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["version"] == "1.0.0"
    assert "timestamp" in data

def test_chat_endpoint_valid(client):
    response = client.post("/chat", json={"message": "Hello FastAPI"})
    assert response.status_code == 200
    data = response.json()
    assert "answer" in data
    assert data["received_message"] == "Hello FastAPI"
    assert "timestamp" in data

def test_chat_endpoint_invalid(client):
    response = client.post("/chat", json={"message": ""})
    assert response.status_code == 422

def test_quiz_endpoint_valid(client):
    response = client.post("/quiz", json={"topic": "Python", "num_questions": 3})
    assert response.status_code == 200
    data = response.json()
    assert data["topic"] == "Python"
    assert data["total_questions"] == 3
    assert len(data["questions"]) == 3
    assert data["questions"][0]["id"] == 1
    assert len(data["questions"][0]["options"]) == 4

def test_quiz_endpoint_invalid(client):
    response = client.post("/quiz", json={"topic": "Python", "num_questions": 50})
    assert response.status_code == 422

def test_summarise_endpoint_valid(client):
    text_input = "FastAPI is a modern web framework. It is fast and easy to learn. It uses Pydantic for validation."
    response = client.post("/summarise", json={"text": text_input, "max_bullets": 2})
    assert response.status_code == 200
    data = response.json()
    assert "summary" in data
    assert len(data["bullets"]) <= 2
    assert data["bullet_count"] <= 2
    assert data["original_length"] == len(text_input)

def test_summarise_endpoint_invalid(client):
    response = client.post("/summarise", json={"text": "Hi", "max_bullets": 2})
    assert response.status_code == 422

