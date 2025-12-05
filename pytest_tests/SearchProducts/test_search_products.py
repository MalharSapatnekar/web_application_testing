from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_user_can_search_products(browser):
    browser.get("https://www.amazon.com")

    search_box = browser.find_element(By.ID, "twotabsearchtextbox")
    search_box.send_keys("Lenovo Tablet")
    search_box.send_keys(Keys.ENTER)

    time.sleep(3)
    results = browser.find_elements(By.CSS_SELECTOR, ".s-title-instructions-style")
    assert len(results) > 0
