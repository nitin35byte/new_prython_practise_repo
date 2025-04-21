import  pytest
import requests
from selenium import webdriver
@pytest.mark.skip
def test_m1():
    a = 3
    b = 4
    assert a+1==b ,"test fail"
    assert  a!=b, "tet test dail"

def test_m2():
    name= "selenium"
    assert name.upper()==name

def test_m3():
    assert True

# from selenium import webdriver
#
# driver =webdriver.Chrome()
# driver.execute_script("window.scrollTo()")
# driver.execute_script("window.scrollby(0, document.body.scrollheight)")
# driver.find_element('arguments[0].window.scrollToView();',)


