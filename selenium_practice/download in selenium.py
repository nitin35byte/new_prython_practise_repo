options = webdriver.ChromeOptions()
prefs = {"download.default_directory": "/path/to/folder"}
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=options)


Tool Tip

tooltip = driver.find_element(By.XPATH, "//button[@id='tooltip_btn']")
tooltip_text = tooltip.get_attribute("title")
assert tooltip_text == "Expected Tooltip"