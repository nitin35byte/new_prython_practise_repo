import time
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://swbedrock-rc.successwareg2.com/")
username=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"username")))
username.send_keys("admin@automation.com")
password=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"password")))
password.send_keys("P@ssw0rd!")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(10)
driver.switch_to.frame("Left-frame")
driver.find_element(By.XPATH,"//button[@class='ant-btn ant-btn-icon-only drawerMenu_inlineButton__ooZ9c ant-btn-link']").click()
driver.find_element(By.XPATH,"//div[normalize-space()='Customer Service']").click()
driver.find_element(By.XPATH,"//a[normalize-space()='Call Handling']").click()
time.sleep(5)
open_tabs=driver.find_elements(By.XPATH,"//div[@class='callTabTitle_tabTitle__1x90j']")
print(len(open_tabs))

driver.find_element(By.XPATH,"//span[normalize-space()='New Phone Call']").click()
serach_box=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Find Your Customer']//..//..//../following-sibling::div[contains(@class,'ant-row')]//div[contains(@class,'searchLocation_searchBar')]")))
serach_box.send_keys("nitin")
serach_box.send_keys(Keys.ENTER)
time.sleep(5)
driver.find_element(By.XPATH,"(//div[contains(@class,'location_locationCard')]//span[contains(@class,'customerButton_tex')])[3]").click()
print("clied")
driver.find_element(By.XPATH,"swID_CallHandling_CallLeftPane_Button_JobRequest").click()
joboption=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,"swID_CallHandling_CallLeftPane_Button_JobRequest")))
joboption.click()

jobclass=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"jobClass")))
select=Select(jobclass)
select.select_by_visible_text("Electrical")