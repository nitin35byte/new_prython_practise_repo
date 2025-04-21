import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.ie.service import Service as IEService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager, IEDriverManager


# Hook to run before tests
def pytest_configure(config):
    # Get browser type from command-line options or default to Chrome
    browser = config.getoption("browser", default="chrome")
    config.browser = browser


# Hook to set up the driver based on browser
@pytest.hookimpl(tryfirst=True)
def pytest_runtest_protocol(item, nextitem):
    browser = item.config.browser

    if browser == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == "edge":
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    elif browser == "ie":
        driver = webdriver.Ie(service=IEService(IEDriverManager().install()))
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    # Add the driver to the test item
    item.driver = driver
    item.driver.maximize_window()
    item.driver.implicitly_wait(10)

    # Run the test
    result = nextitem()

    # Teardown: Quit the driver after the test
    driver.quit()

    return result
