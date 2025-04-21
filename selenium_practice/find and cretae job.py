import time
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
driver.get("https://swbedrock-rc.successwareg2.com/login")
username=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"username")))
username.send_keys("admin@automation.com")
password=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"password")))
password.send_keys("P@ssw0rd!")
driver.find_element(By.XPATH,"//button[@type='submit']").click()

time.sleep(10)
driver.maximize_window()
driver.switch_to.frame("Left-frame")
menu=WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,"//button[@class='ant-btn ant-btn-icon-only drawerMenu_inlineButton__ooZ9c ant-btn-link']")))
# driver.find_element(By.XPATH,"//button[@class='ant-btn ant-btn-icon-only drawerMenu_inlineButton__ooZ9c ant-btn-link']").click()
menu.click()
driver.find_element(By.XPATH,"//div[normalize-space()='Customer Service']").click()
driver.find_element(By.XPATH,"//a[normalize-space()='Call Handling']").click()
time.sleep(5)
open_tabs=driver.find_elements(By.XPATH,"//div[@class='callTabTitle_tabTitle__1x90j']")
print(len(open_tabs))
driver.find_element(By.XPATH,"//span[normalize-space()='New Phone Call']").click()
searchbar=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//span[text()='Find Your Customer']//..//..//../following-sibling::div[contains(@class,'ant-row')]//div[contains(@class,'searchLocation_searchBar')]//input")))
   # driver.find_element(By.XPATH,"//span[text()='Find Your Customer']//..//..//../following-sibling::div[contains(@class,'ant-row')]//div[contains(@class,'searchLocation_searchBar')]//input"))
searchbar.click()
searchbar.send_keys("xzxz xaasasa")
searchbar.send_keys(Keys.ENTER)
driver.find_element(By.XPATH,"(//span[@class='customerButton_text__1zwps'])[1]").click()
print("success")