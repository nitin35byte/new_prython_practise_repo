# import requests
# import  pytest
#
# HEADERS={
#             "Authorization":"eyJhbGciOiJSUzI1NiJ9.eyJ0ZW5hbnRfaWQiOm51bGwsImVycm9yX21lc3NhZ2UiOiJXZeKAmXJlIHNvcnJ5LCB0aGUgaW5mb3JtYXRpb24gZW50ZXJlZCBkb2VzIG5vdCBtYXRjaCBvdXIgcmVjb3Jkcy4gUGxlYXNlIHJlLWVudGVyIG9yIGNvbnRhY3Qgc3lzdGVtIGFkbWluaXN0cmF0b3IuIiwibWFzdGVyX2lkIjpudWxsLCJzdWIiOiJhZG1pbkBhdXRvbWF0aW9uLmNvbSIsInVzZXJfbmFtZSI6ImFkbWluQGF1dG9tYXRpb24uY29tIiwiZGJfY2x1c3Rlcl90YWciOm51bGwsIm9yZ19zY29wZSI6bnVsbCwidGltZV96b25lIjpudWxsLCJjbGllbnRfaWQiOm51bGwsIndhcm5pbmdfbWVzc2FnZSI6bnVsbCwicGFzc3dvcmQiOm51bGwsImZ1bGxfbmFtZSI6bnVsbCwicmVzZXRfdXNlcl9wd2QiOmZhbHNlLCJhcGlfZGlyZWN0aW9uIjoiR0VOMiIsInJlc3RyaWN0ZWQiOmZhbHNlLCJjb21wYW55X25hbWUiOm51bGwsIm9yZ2FuaXphdGlvbl9pZCI6bnVsbCwic2NvcGUiOm51bGwsImNvbXBhbnlfbm8iOm51bGwsImV4cCI6MTc0MjMxNTM1MiwiaWF0IjoxNzQyMzE1MzUyLCJqdGkiOiJlMmM0YjUxYy03OGMyLTRiYTUtYjMyMi0yNWI4MjBkZDMwNmEiLCJ1c2VybmFtZSI6ImFkbWluQGF1dG9tYXRpb24uY29tIn0.z3vuTqCiaHkUCX3WopNnG7eLFEY2fUU3hEGY9zj71dmdPspyQGmZH7FppueL6WvZ9lrZgi3afzld5-FglcrHP7Attb8FYrLGR-LH0BKeAKRBSilslE_1ZA1fkX6Hc-D6HA7XgIM1qxwC8BvfEPH3dCdiV1sTCHYuVGgEPlDctV-I4N1OACwYFRYPb7c-F04upROcLMGTTeSrMlDM8UgmIYt0c9BM8fkG2yTY2DGZVGv4zorVxqYePS6ybePqbXOlS9gcBNRYMPr3J2mPYoJBki5WMj6v_npcukKt0nJqiVMQw53BezAHqNsFs8GThTmOcsEy60JRVEJu5NPpNHj7Qen3x7hlh2WGQ_X955PdMEfmqr6KrPOHqac439Deb53BNGMkV6TPMPeJrWI02Jcs-oB25twm0WNiG8uup4UHLHp-zbrXXWurEjx-pTJRexo1hkOqWunAR-4a_mxL--BUPMXsgltYYedWk3-bMNH7xXJ4uVjKnACkiUcVIkHjF2ZQ",
#             "Content-Type": "application/json"
#            }
#
# query={
#         "input": {
#             "sessionRequest": {
#                 "addCallerID": {
#                     "callKey": "112313",
#                     "userKey": "testautomation",
#                     "callerNumber": "1198988426",
#                     "dnis": "9898442",
#                     "callerName": "Test",
#                     "street": "Test Street",
#                     "city": "New York",
#                     "state": "NY",
#                     "zip": "11012"
#                 }
#             }
#         }
#     }
# base_url="https://publicapi-uat.successwareg2.com/api"
# response=requests.post(base_url,headers=HEADERS , json=query)
# print(response.status_code)

import pytest
import requests
import pytest

# Define constants for reusability


# @pytest.mark.api
# def test_graphql_api():
#
#     """Test a GraphQL API request"""
#     response = requests.post(f"{base_url}/graphql", headers=HEADERS, json=query)
#
#     # Debugging information
#     print("Response Status Code:", response.status_code)
#     print("Response Body:", response.text)
#
#     # Assertions
#     assert response.status_code == 200, "API request failed"
#     json_data = response.json()
#     print(json_data)

    # Check if response contains expected data
    # assert "data" in json_data, "Response is missing 'data' key"
    # assert "user" in json_data["data"], "'user' field is missing"
    # assert isinstance(json_data["data"]["user"], dict), "'user' should be a dictionary"

def test_auth_key():
    login_url="https://swbedrock-uat.successwareg2.com/web/bedrock"
    credentials = {
        "username": "admin@automation.com",
        "password":"P@ssw0rd!",
        "companyName": "[TEST] Automation"
        }
    response=requests.post(f"{login_url}/login",json=credentials)
    print(response.status_code)
    assert response.status_code == 200
    print(response.json())
    assert response.headers["Content-Type"].startswith("application/json")
