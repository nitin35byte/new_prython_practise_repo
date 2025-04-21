import time

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

BASE_URL = "https://jsonplaceholder.typicode.com"
HEADERS = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}


def test_retry():
    """Test API retry logic for rate limits (429 Too Many Requests)"""

    session = requests.Session()

    # Configure retry logic
    retries = Retry(
        total=3,  # Number of retry attempts
        backoff_factor=2,  # Exponential backoff (2, 4, 8 sec)
        status_forcelist=[429, 500],  # Retry only for these status codes
        allowed_methods=["GET", "POST"]
    )

    session.mount("https://", HTTPAdapter(max_retries=retries))

    headers = {"Authorization": "Bearer INVALID_TOKEN"}
    response = session.get(f"{BASE_URL}/posts", headers=headers)

    assert response.status_code in [200, 429]  # Expect success or retry failure

def test_response():
    payload = {
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
    start_time=time.time()
    response = requests.post(f"{BASE_URL}/users", headers=HEADERS, json=payload)
    end_time=time.time()
    actual_time= end_time - start_time
    assert actual_time <10
    assert response.json()['name']=='John Doe'
    assert response.headers["Content-Type"].startswith("Application/json")

