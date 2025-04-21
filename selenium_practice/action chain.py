from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC



driver = webdriver.Chrome()

driver.get("")
action =ActionChains(driver)
drag=driver.find_element(By.XPATH ,"")
drop=driver.find_element(By.XPATH ,"")
action.drag_and_drop(drag , drop).perform()
action.click()
action.move_to_element()
action.context_click()
alert=driver.switch_to.alert
action.send_keys().perform()