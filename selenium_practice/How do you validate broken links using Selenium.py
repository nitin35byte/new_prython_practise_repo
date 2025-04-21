import requests
from selenium.webdriver.common.by import By

links = driver.find_elements(By.TAG_NAME, "a")
for link in links:
    url = link.get_attribute("href")
    response = requests.head(url)
    print(f"{url} : {response.status_code}")
