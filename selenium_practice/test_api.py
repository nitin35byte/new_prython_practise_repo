import requests
import pytest

BASE_URL = "https://api.example.com"
HEADERS = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

def test_get_users():
    """Test the GET /users endpoint."""
    response = requests.get(f"{BASE_URL}/users", headers=HEADERS)
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Assuming the response is a list of users

def test_create_user():
    """Test the POST /users endpoint."""
    payload = {
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
    response = requests.post(f"{BASE_URL}/users", headers=HEADERS, json=payload)
    assert response.status_code == 201
    response_data = response.json()
    assert response_data["name"] == "John Doe"
    assert response_data["email"] == "john.doe@example.com"

def test_create_user_missing_field():
    """Test the POST /users endpoint with missing fields."""
    payload = {
        "name": "John Doe"
    }
    response = requests.post(f"{BASE_URL}/users", headers=HEADERS, json=payload)
    assert response.status_code == 400
    response_data = response.json()
    assert "email" in response_data["error"]["message"]
    response.json().headers["Content-Type"].starwith("Application/Json")