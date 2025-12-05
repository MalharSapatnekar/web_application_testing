import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_search_pagination_next_page(browser):
    wait = WebDriverWait(browser, 30)

    browser.get("https://www.amazon.com")
    time.sleep(2)

    # search
    search = wait.until(
        EC.visibility_of_element_located((By.ID, "twotabsearchtextbox"))
    )
    search.send_keys("usb cable")
    search.submit()

    # wait for results
    wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.s-main-slot"))
    )
    time.sleep(2)

    # scroll down so pagination is visible
    for _ in range(4):
        browser.execute_script("window.scrollBy(0, 800);")
        time.sleep(1)

    # click 'Next' (s-pagination-next)
    next_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.s-pagination-next"))
    )
    browser.execute_script("arguments[0].click();", next_button)
    time.sleep(3)

    #-verify results on next page
    results = browser.find_elements(
        By.CSS_SELECTOR, "div.s-main-slot div[data-component-type='s-search-result']"
    )
    assert len(results) > 0, "No search results found on page 2"
