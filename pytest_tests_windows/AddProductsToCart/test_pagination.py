import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.tc_id("TC-PYT-001")
def test_pagination(browser):
    wait = WebDriverWait(browser, 30)

    browser.get("https://www.amazon.com")

    # Step 1 — Search “Bluetooth Speaker”
    search = wait.until(EC.element_to_be_clickable((By.ID, "twotabsearchtextbox")))
    search.send_keys("Bluetooth Speaker")
    search.submit()

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.s-main-slot")))
    time.sleep(2)

    # Step 2 — Capture page 1 results count
    items_page1 = len(browser.find_elements(By.CSS_SELECTOR, "div.s-main-slot div[data-component-type='s-search-result']"))
    assert items_page1 > 5

    # Step 3 — Click next page
    next_btn = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.s-pagination-next"))
    )
    browser.execute_script("arguments[0].click();", next_btn)

    # Step 4 — Wait for page 2
    time.sleep(3)
    items_page2 = len(browser.find_elements(By.CSS_SELECTOR, "div.s-main-slot div[data-component-type='s-search-result']"))

    assert items_page2 > 5, "Pagination did not load results"
