import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"  # Sample API

@pytest.mark.parametrize("endpoint, expected_status", [
    ("/posts", 200),       # Test GET all posts
    ("/posts/1", 200),     # Test GET single post
    ("/invalid", 404)      # Test invalid endpoint
])
def test_get_api_responses(endpoint, expected_status):
    """Test GET API status codes"""
    response = requests.get(BASE_URL + endpoint)
    assert response.status_code == expected_status

def test_create_post():
    """Test POST API - Create a new post"""
    payload = {"title": "Test Post", "body": "Test Content", "userId": 1}
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    assert response.status_code == 201
    assert response.json()["title"] == payload["title"]

def test_update_post():
    """Test PUT API - Update a post"""
    payload = {"title": "Updated Title", "body": "Updated Content", "userId": 1}
    response = requests.put(f"{BASE_URL}/posts/1", json=payload)
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Title"

def test_delete_post():
    """Test DELETE API - Remove a post"""
    response = requests.delete(f"{BASE_URL}/posts/1")
    assert response.status_code == 200

def test_invalid_token():
    """Test API with invalid authentication token"""
    headers = {"Authorization": "Bearer INVALID_TOKEN"}
    response = requests.get(f"{BASE_URL}/posts", headers=headers)
    assert response.status_code == 401  # Unauthorized

def test_retry():
    """Test API with invalid authentication token"""
    headers = {"Authorization": "Bearer INVALID_TOKEN"}
    response = requests.get(f"{BASE_URL}/posts", headers=headers)
    assert response.status_code == 429  # Unauthorized
    response.retry
