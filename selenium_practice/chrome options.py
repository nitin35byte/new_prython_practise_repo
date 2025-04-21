from optparse import Option

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options= Options()
options.add_argument("--headless")
options.add_argument("--disable-extensions")
options.add_argument('-incognito')
prefs = {"profile.manage_default_content_setting.image":2}
options.add_experimental_option("prefs" , prefs)
driver = webdriver.Chrome(options=options)
driver.get("")


"""
200 OK: The request was successful.
201 Created: The resource was successfully created.
400 Bad Request: The request was malformed.
401 Unauthorized: Authentication is required.
403 Forbidden: The user does not have permission to access the resource.
404 Not Found: The requested resource could not be found.
500 Internal Server Error: The server encountered an error while processing the request
"""




driver.execute_script("window.scrollBy(0 , 500)")
driver.execute_script("argumen[0].scrollInToview(True):")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

import configparser
