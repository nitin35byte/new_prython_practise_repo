import pytest
from pytest_bdd import scenario, given, when, then

# Link the scenario from the feature file
@scenario("login.feature", "Successful login")
def test_successful_login():
    pass  # This serves as a placeholder


# Step Definitions
@given("I am on the login page")
def open_login_page():
    print("Opening login page")

@when("I enter valid username and password")
def enter_credentials():
    print("Entering username and password")

@then("I should be redirected to the homepage")
def verify_homepage():
    print("User is on the homepage")
