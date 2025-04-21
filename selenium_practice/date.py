import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common import  keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def datepicke(Target_day , Expected_year , Expected_month):
    while True:
        try:
            data_deader=WebDriverWait(driver,15).until(EC.visibility_of_element_located((By.XPATH,"//div[@class='DayPicker-Caption']")))
            data=data_deader.text
            print(data)
            extracted_month=data.split()[0]
            extracted_year=data.split()[1]

            if extracted_month ==Expected_month and int(extracted_year)==Expected_year:
                driver.find_element(By.XPATH,f"(//p[normalize-space()='{Target_day}'])[1]").click()
                break
            else:
                next_month=WebDriverWait(driver , 10).until(EC.element_to_be_clickable((By.XPATH,"//span[@aria-label='Next Month']")))
                next_month.click()
            time.sleep(2)
        except Exception as e:
            print(e)

driver=webdriver.Chrome()
driver.get("https://www.makemytrip.com/")
cookie=driver.get_cookies()
print(cookie)
driver.maximize_window()
title=driver.title
print(title)
assert title=='MakeMyTrip - #1 Travel Website 50% OFF on Hotels, Flights & Holiday'
time.sleep(5)
driver.find_element(By.XPATH,"//span[contains(@class,'commonModal')]").click()
driver.find_element(By.ID,"fromCity").click()
driver.find_element(By.XPATH,"(//input[contains(@type,'text')])[2]").send_keys("ran")
time.sleep(2)
board_location=driver.find_elements(By.XPATH,"//p[contains(@class,'searchedResult')]")
for location in board_location:
    l=location.text
    print(l)
    if l =="Deoghar Airport":
        location.click()
time.sleep(2)

departure=WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.XPATH,"//label[@for='departure']")))
departure.click()

Target_day = 15
Expected_year=2025
Expected_month ="June"
datepicke(Target_day , Expected_year , Expected_month)
