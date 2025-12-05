import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    gecko_path = "geckodriver"

    driver = webdriver.Firefox(executable_path=gecko_path)
    driver.maximize_window()

    yield driver
    driver.quit()
