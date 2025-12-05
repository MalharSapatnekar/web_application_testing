import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    gecko_path = "/home/CyFast/geckodriver"   # Linux driver discovered by `which`

    driver = webdriver.Firefox(executable_path=gecko_path)
    driver.maximize_window()

    yield driver
    driver.quit()
