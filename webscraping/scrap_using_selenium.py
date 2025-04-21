from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Navigate to the target webpage
driver.get("https://www.goat.com/sneakers")

try:
    # Wait for the sneaker elements to be loaded
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='GridStyles__GridCellWrapper-sc-1cm482p-0 hiXKdk']"))
    )

    # Loop through a range of indices to locate and print prices
    for i in range(1, 100):
        # Locate the price element for the current sneaker
        price_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, f"(//span[@class='LocalizedCurrency__Amount-sc-yoa0om-0 jDDuev'])[position()={i}]"))
        )

        # Extract the text of the price element
        price = price_element.text

        # Print the price value
        print(f"Price {i}: {price}")

except Exception as e:
    print("An error occurred:", e)

finally:
    # Close the WebDriver session
    driver.quit()
