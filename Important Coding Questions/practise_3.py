import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from urllib.parse import urljoin

# Setup WebDriver in headless mode
options = Options()
options.add_argument("--headless")

driver = webdriver.Chrome(options=options)
driver.get("https://www.amazon.in/")
time.sleep(10)  # Wait for the page to load

# Find all <a> tags (links)
all_links = driver.find_elements(By.TAG_NAME, "a")

valid_links = []

for link in all_links:
    url = link.get_attribute("href")

    # Check if the URL is not None and is not empty
    if url:
        # Handle relative URLs
        url = urljoin("https://www.amazon.in", url)

        try:
            # Make a HEAD request to the URL
            response = requests.head(url)
            if response.status_code == 200:
                valid_links.append(url)  # Add valid URLs to the list
            else:
                print(f"Broken link: {url}")
        except requests.RequestException as e:
            print(f"Error with {url}: {e}")
    else:
        print("No href found for link")

# Print all valid links
print("Valid links:")
for valid_link in valid_links:
    print(valid_link)

driver.quit()  # Don't forget to close the driver
