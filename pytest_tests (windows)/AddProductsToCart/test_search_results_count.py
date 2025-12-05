from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.mark.tc_id("TC-PYT-005")
def test_search_results_count(browser):
    browser.get("https://www.amazon.com")
    wait = WebDriverWait(browser, 20)

    # search
    search_box = wait.until(
        EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
    )
    search_box.send_keys("Laptop")
    search_box.submit()

    # wait for at least ONE result
    results = wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "div[data-component-type='s-search-result']")
        )
    )

    assert len(results) >= 1, f"Expected at least 1 result, got {len(results)}"
