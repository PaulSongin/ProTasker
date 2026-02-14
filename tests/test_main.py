import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_home_page():
    response = client.get("/")
    assert response.status_code == 200

def test_get_tasks_list():
    response = client.get("/tasks/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_user_simple():
    import uuid
    random_email = f"{uuid.uuid4()}@test.com"
    response = client.post(
        "/register",
        json={"email": random_email, "password": "password123"}
    )
    assert response.status_code == 201