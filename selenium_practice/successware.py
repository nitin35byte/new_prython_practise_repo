import time
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.get("https://swbedrock-uat.successwareg2.com/login")
username=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"username")))
username.send_keys("admin@automation.com")
password=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"password")))
password.send_keys("Password@123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()

time.sleep(10)
driver.maximize_window()
titl=driver.title
print(titl)
# assert titl=="My Dashboard - [TEST] Automation"

iframes = driver.find_elements(By.TAG_NAME, "iframe")
print(f"Number of iframes on the page: {len(iframes)}")

for index, iframe in enumerate(iframes):
    print(f"iframe {index}: ID = {iframe.get_attribute('id')}, Name = {iframe.get_attribute('name')}")


driver.switch_to.frame("Left-frame")
menu=WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,"//button[@class='ant-btn ant-btn-icon-only drawerMenu_inlineButton__ooZ9c ant-btn-link']")))
# driver.find_element(By.XPATH,"//button[@class='ant-btn ant-btn-icon-only drawerMenu_inlineButton__ooZ9c ant-btn-link']").click()
menu.click()
driver.find_element(By.XPATH,"//div[normalize-space()='Customer Service']").click()
driver.find_element(By.XPATH,"//a[normalize-space()='Call Handling']").click()
time.sleep(5)
open_tabs=driver.find_elements(By.XPATH,"//div[@class='callTabTitle_tabTitle__1x90j']")
print(len(open_tabs))
# for tab in range(open_tabs:
#     try:
#         tab.click()
#         cancel_button=driver.find_element(By.XPATH,"//div[contains(@class,'ant-tabs-tabpane ant-tabs-tabpane-active')]//header[contains(@class,'header_header__24ckF')]//button[contains(@type,'button')]")
#         if cancel_button==True:
#             cancel_button.click()
#     except Exception as e:
#         print(e)
#


driver.find_element(By.XPATH,"//span[normalize-space()='New Phone Call']").click()
driver.find_element(By.CSS_SELECTOR,"div[class='ant-tabs-tabpane ant-tabs-tabpane-active'] div[class='call_container__2IGbX'] div[class='call_body__3Vkg4'] section[class='call_rightPane__2H8ET'] div[class='card_contentArea__2QK2b searchPane_customerAreaWithLocation__KvwGg'] div[class='card_withRightArea__3usE5'] div button[type='button'] span").click()

driver.find_element(By.ID,"firstName").send_keys("NitinNitin")   
driver.find_element(By.ID,"lastName").send_keys("NitinNitin")
driver.find_element(By.XPATH,"//input[@name='phoneNumber']").send_keys("0000123")
driver.find_element(By.ID,"email").send_keys("NitinNitin@sw.com")

driver.find_element(By.ID,"leadSourceTypeId").click()
driver.find_element(By.XPATH,"//div[contains(text(),'CLUB')]").click()
driver.find_element(By.ID,"leadSourceId").click()
driver.find_element(By.XPATH,"//div[contains(text(),'TELE-Telemarketing')]").click()
# entermanualaddress = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[class='ant-btn customerForm_enterLink__EVlrO ant-btn-link']")))
# entermanualaddress.click()
input_address=WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,"(//input[@id='location.search'])[1]")))
input_address.send_keys("1111")
#driver.find_element(By.XPATH,"(//input[@id='location.search'])[1]").send_keys("1111")
address=Select(WebDriverWait(driver , 20).until(EC.visibility_of_element_located((By.XPATH,"(//div[@class='ant-select-item ant-select-item-option'])[1]"))))  #(//div[@class='ant-select-item-option-content'])[1]
address.select_by_visible_text("1111 Polaris Parkway, Columbus, OH, USA")
#driver.find_element(By.XPATH,"(//div[@class='ant-select-item-option-content'])[1]").click()

# driver.find_element(By.XPATH,"//input[@id='location.city']").send_keys("delhi")
# driver.find_element(By.XPATH,"//input[@id='location.state']").send_keys("de")
# driver.find_element(By.XPATH,"//input[@id='location.zipCode']").send_keys("110011")
driver.find_element(By.XPATH,"//span[normalize-space()='Create Customer']").click()

success_text=driver.find_element(By.XPATH,"//p[contains(@class,'message_description')]")
print(success_text.text)
