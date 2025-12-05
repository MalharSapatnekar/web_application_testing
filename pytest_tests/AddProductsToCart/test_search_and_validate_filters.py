import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def close_location_popup_if_present(browser):
    """Closes Amazon's location popup (if shown)."""
    try:
        time.sleep(2)

        # Close button inside popup
        close_btn = browser.find_element(
            By.CSS_SELECTOR, "button#glow-ingress-block, div#glow-ingress-block"
        )
        close_btn.click()
        time.sleep(1)
        return
    except:
        pass

    # Alternative popup versions
    try:
        dismiss = browser.find_element(By.ID, "nav-global-location-popover-link")
        browser.execute_script("arguments[0].click();", dismiss)
        time.sleep(1)
    except:
        pass


def test_search_and_validate_filters(browser):
    browser.get("https://www.amazon.com")
    wait = WebDriverWait(browser, 30)

    # Search product
    search_box = wait.until(
        EC.visibility_of_element_located((By.ID, "twotabsearchtextbox"))
    )
    search_box.send_keys("Laptop")
    search_box.submit()

    # Wait for results
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.s-main-slot")))

    # Close popup if blocking left sidebar
    close_location_popup_if_present(browser)

    # Scroll to left filter sidebar
    browser.execute_script("window.scrollBy(0, 600)")
    time.sleep(2)

    # Find filter headers
    filter_headers = browser.find_elements(
        By.CSS_SELECTOR,
        "span.a-size-base.a-color-base, span.a-size-base-plus, span.a-text-bold"
    )
    assert len(filter_headers) > 0, "Filter headers not found"

    # Find ANY filter checkbox reliably
    checkboxes = browser.find_elements(
        By.CSS_SELECTOR, "li[id*='p_'], i.a-icon.a-icon-checkbox"
    )
    assert len(checkboxes) > 0, "No filter checkboxes found"

    # Scroll and click safely
    first_checkbox = checkboxes[0]

    browser.execute_script("arguments[0].scrollIntoView(true);", first_checkbox)
    time.sleep(1)

    browser.execute_script("arguments[0].click();", first_checkbox)

    # Validate page reload
    wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.s-main-slot"))
    )
