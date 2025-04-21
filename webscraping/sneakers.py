from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Navigate to the target webpage
driver.get("https://www.goat.com/sneakers")

# Locate all price elements matching the XPath
price_elements = driver.find_elements(By.XPATH, "//span[@class='LocalizedCurrency__Amount-sc-yoa0om-0 jDDuev']")

# Iterate through the price elements and print their text (prices)
for i, price_element in enumerate(price_elements, start=1):
    price = price_element.text
    ##print(f"Price {i}: {price}")
shoes_name = driver.find_elements(By.XPATH,"//div[@class='GridCellProductInfo__Name-sc-17lfnu8-3 iPovsV']")

for i, shoe_name_element in enumerate(shoes_name, start=1):
        name = shoe_name_element.text
        ##print(f"Shoe {i}: {name}")


posted_date=driver.find_elements(By.XPATH,"//div[@class='GridCellProductInfo__Year-sc-17lfnu8-2 hyAqZs']")

for i in posted_date:
    dates=i.text
    print(dates)
# Close the WebDriver session



driver.quit()
