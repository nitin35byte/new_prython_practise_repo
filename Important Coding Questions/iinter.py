# class Login:
#
#     xpath_username=""
#     xpath_id=""
#     xpath_login_btn=""
#
#
#     def __init__(self,driver):
#         self.driver=driver
#
#
#
#     def userName(self):
#         self.driver.find_element(By.Xpath,self.xpath_username)
#
#     def password(self):
#         self.driver.find_element(By.Xpath,self.xpath_id)
#
#     def subBtner(self):
#         self.driver.find_element(By.Xpath, self.xpath_login_btn)
#
# from paggeBject import testFile
#
# self.lp=Login
# self.lp.userName.send_keys(user_name)
# self.lp.password.send_keys("testdata")
# self.lp.subBtner.click()
#
#
# import pandas as pd
#
# df=pd.read_csv("test.csv")
#
# df["name"].tolist()
#
# user_name=df["name"][1]
#
# *** Setting ***
#
# Library     SeleniumLibrary
#
# *** Varibale ***
# ${url}=     test.com
# ${xpath_user_name_value}
# ${user_name_value}=   test
# ${xpath_password_value}
# ${password_value}=        password
# ${login_btn}=       login_btn
#
# *** Keyword ***
# Login Functionalty
#     Open Browser        ${url}      chrome
#     Sleep   5s
#     Input       ${xpath_user_name_value}    ${user_name}
#     Sleep   5s
#     Input       ${xpath_password_value}     ${password_value}
#     Click Element   ${login_btn}
#
# *** Test Cases ***
# Validate Login Functionality
#     Login Functionalty
#
#
# with open("test.josn",'r') as f:
#     a=f.load()
#     a.readlibes

# Using Python’s requests library, write a function to:
# Send a POST request to /api/login with credentials
# Store the returned token
# Use that token to send a GET request to /api/dashboard and return the response
import requests
base_url=""
def login():
    payload=""
    headers={"username":"username",
             "password":"password"}

    response=requests.post(f"{base_url}",headers=headers  , json=payload)
    token=response.json()
    return token


def dashboard():
    response = requests.get(f"{base_url}", headers=token)
    print(response.json())