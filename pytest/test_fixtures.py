import pytest
from selenium import webdriver

# @pytest.fixture(params=["chrome", "edge", "IE"])
# def test_browser(request):
#     if request.params == "chrome":
#         driver = webdriver.Chrome()
#
#     elif request.params == "edge":
#         driver = webdriver.Edge()
#
#     elif request.params == "IE":
#         driver = webdriver.Ie
#
#     yield driver

    # driver.quit()

# @pytest.mark.parametrize('a,b,c' ,[(2,4,6),(2,5,7)])
# def test_parametrization(a,b,c):
#     assert a+b==c

import pytest

@pytest.mark.parametrize("a, b, c", [(2, 4, 6), (2, 5, 7)])
def test_parametrization(a, b, c):
    assert a + b == c
