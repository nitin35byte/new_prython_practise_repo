from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")

# Get the main window handle
main_window = driver.current_window_handle
print("Main Window Handle:", main_window)

# Open a new window using JavaScript
driver.execute_script("window.open('https://www.bing.com');")
time.sleep(2)

# Get all window handles
all_windows = driver.window_handles
print("All Window Handles:", all_windows)

# Switch to the new window (last in the list)
driver.switch_to.window(all_windows[-1])
print("Switched to new window:", driver.title)

# Close the new window and switch back
driver.close()
driver.switch_to.window(main_window)
print("Switched back to main window:", driver.title)

driver.quit()
