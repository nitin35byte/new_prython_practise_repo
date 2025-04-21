import requests
from selenium import webdriver

links = driver.find_elements(By.TAG_NAME, "a")

for link in links:
    url = link.get_attribute("href")
    response = requests.head(url)
    if response.status_code != 200:
        print(f"Broken link: {url}")
