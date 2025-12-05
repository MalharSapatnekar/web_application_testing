import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def close_all_popups(driver):
    try:
        driver.execute_script("""
            let p = document.getElementById('nav-global-location-popover-link');
            if (p) p.style.display='none';
        """)
    except:
        pass


def test_price_filter(browser):
    browser.get("https://www.amazon.com")
    wait = WebDriverWait(browser, 40)
    time.sleep(2)

    close_all_popups(browser)

    # Search product
    search = wait.until(
        EC.element_to_be_clickable((By.ID, "twotabsearchtextbox"))
    )
    search.clear()
    search.send_keys("Laptop")
    search.submit()

    # Wait for results
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.s-main-slot")))
    time.sleep(2)

    # Step 3 — Scroll to filter area
    browser.execute_script("window.scrollBy(0, 800)")
    time.sleep(2)

    # Find ANY price chip (Under $25 / $200 & above / similar)
    chips = browser.find_elements(By.CSS_SELECTOR, "span.a-size-base")
    chips = [c for c in chips if any(keyword in c.text for keyword in ["Under", "$", "₹", "Over"])]

    assert len(chips) > 0, "No price filter chips found"

    chip = chips[0]
    browser.execute_script("arguments[0].scrollIntoView(true);", chip)
    time.sleep(1)
    browser.execute_script("arguments[0].click();", chip)

    # Wait for filtered results page to load
    time.sleep(3)
    browser.execute_script("window.scrollTo(0, 0)")
    time.sleep(1)

    # MOST RELIABLE RESULTS LOCATOR
    results = wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "div[data-component-type='s-search-result']")
        )
    )

    assert len(results) > 0, "No products displayed after applying price filter"

    # Extra validation: check first product title exists
    first_title = results[0].find_element(By.CSS_SELECTOR, "h2")
    assert first_title.text.strip() != "", "First result has no title"
