import pytest
import requests

# TC_001 - Verify GET all users
def test_get_all_users(api):
    response = api.get("/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# TC_002 - Verify GET single user
@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_get_single_user(api, user_id):
    response = api.get(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["id"] == user_id

# TC_003 - Verify POST new user
def test_create_new_user(api):
    payload = {"name": "John Doe", "email": "john.doe@example.com"}
    response = api.post("/users", data=payload)
    assert response.status_code == 201
    assert response.json()["name"] == "John Doe"

# TC_004 - Verify PUT update user
def test_update_user(api):
    user_id = 1
    payload = {"name": "Updated Name"}
    response = api.put(f"/users/{user_id}", data=payload)
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Name"

# TC_005 - Verify DELETE user
def test_delete_user(api):
    user_id = 1
    response = api.delete(f"/users/{user_id}")
    assert response.status_code == 200

# TC_006 - Verify unauthorized access
def test_unauthorized_access(api):
    headers = {"Authorization": "Invalid_Token"}
    response = api.get("/protected/resource", headers=headers)
    assert response.status_code == 401
    assert "Unauthorized" in response.text

# TC_007 - Verify API with invalid input
def test_invalid_input(api):
    payload = {"name": ""}  # Invalid name
    response = api.post("/users", data=payload)
    assert response.status_code == 400
    assert "error" in response.text

# TC_008 - Verify response time < 2 sec
def test_response_time(api):
    response = api.get("/users")
    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 2

# TC_009 - Verify pagination
def test_pagination(api):
    response = api.get("/users", params={"page": 2})
    assert response.status_code == 200
    assert "page" in response.text

# Pagination
def test_api_pagination():
    response = requests.get(f"{BASE_URL}/users?page=2")
    assert response.status_code == 200

    data = response.json()
    assert len(data["users"]) == 10  # Assuming 10 users per page
    assert "next_page" in data  # Verify next page exists

# Large Payload
def test_large_payload():
    large_payload = [{"name": f"user{i}", "email": f"user{i}@mail.com"} for i in range(1000)]

    response = requests.post(f"{BASE_URL}/bulk_users", json=large_payload)
    assert response.status_code == 201
    assert response.json()["message"] == "Users created successfully"
