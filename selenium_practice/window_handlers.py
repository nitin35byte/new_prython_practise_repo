import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Setup WebDriver
driver = webdriver.Chrome()
driver.get("https://www.flipkart.com/")
main_window = driver.current_window_handle  # Store main window handle
print("Current Page Title:", driver.title)
time.sleep(4)

# Scroll down
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Click on Myntra (if it's in the search results)
try:
    myntra_link = driver.find_element(By.XPATH, "//a[contains(@href, 'myntra.com')]")
    myntra_link.click()
    time.sleep(5)

    # Switch to the new window
    all_windows = driver.window_handles
    for window in all_windows:
        if window != main_window:
            driver.switch_to.window(window)
            break

    print("Myntra Page Title:", driver.title)
    driver.close()  # Close Myntra tab and switch back
    driver.switch_to.window(main_window)
except Exception as e:
    print("Myntra link not found:", e)

# Navigate Back
driver.back()
time.sleep(5)

# Scroll Down Again
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Click on Cleartrip
try:
    cleartrip_link = driver.find_element(By.XPATH, "//a[contains(@href, 'cleartrip.com')]")
    cleartrip_link.click()
    time.sleep(5)

    # Switch to Cleartrip window
    all_windows = driver.window_handles
    for window in all_windows:
        if window != main_window:
            driver.switch_to.window(window)
            break

    print("Cleartrip Page Title:", driver.title)
    driver.close()  # Close Cleartrip tab and switch back
    driver.switch_to.window(main_window)
except Exception as e:
    print("Cleartrip link not found:", e)

# Close Browser
driver.quit()


