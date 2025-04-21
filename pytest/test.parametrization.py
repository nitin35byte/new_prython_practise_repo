import pytest

@pytest.mark.parametrize("num", [1, 2, 3, 4])
def test_check_even(num):
    assert num % 2 == 0, f"{num} is not even"


@pytest.mark.parametrize("a, b, expected", [(2, 3, 5), (4, 6, 10), (5, 5, 10)])
def test_addition(a, b, expected):
    assert a + b == expected


import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def setup():
    driver = webdriver.Chrome()  # Initialize WebDriver
    driver.get("https://example.com/login")  # Open website
    yield driver  # Provide driver to test function
    driver.quit()  # Quit after test

@pytest.mark.parametrize("username, password", [
    ("testuser1", "password1"),
    ("testuser2", "password2"),
    ("testuser3", "password3"),
])
def test_login(setup, username, password):
    driver = setup
    driver.find_element(By.ID, "username").send_keys(username)  # Enter username
    driver.find_element(By.ID, "password").send_keys(password)  # Enter password
    driver.find_element(By.ID, "loginButton").click()  # Click login button

    # Check if login is successful
    assert "Dashboard" in driver.title



