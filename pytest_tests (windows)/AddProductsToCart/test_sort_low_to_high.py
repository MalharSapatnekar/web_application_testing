import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.tc_id("TC-PYT-006")
def test_sort_low_to_high(browser):
    wait = WebDriverWait(browser, 40)

    # Direct sorted URL – avoids search bar problems
    browser.get("https://www.amazon.com/s?k=laptop&s=price-asc-rank")

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.s-main-slot")))
    time.sleep(3)

    # Scroll multiple times to load many items
    for _ in range(15):
        browser.execute_script("window.scrollBy(0, 900);")
        time.sleep(1)

    # COLLECT from ALL PRICE SELECTORS
    price_selectors = [
        "span.a-price > span.a-offscreen",
        "span.a-price.a-text-price > span.a-offscreen",
        "span[data-a-color='price'] span.a-offscreen",
        "span[class*='a-price'] span.a-offscreen"
    ]

    prices = []
    seen = set()

    for selector in price_selectors:
        elements = browser.find_elements(By.CSS_SELECTOR, selector)
        for el in elements:
            try:
                txt = el.get_attribute("innerText").replace("$", "").replace(",", "").strip()
                if txt and txt.replace(".", "", 1).isdigit():
                    val = float(txt)
                    if val not in seen:
                        seen.add(val)
                        prices.append(val)
            except:
                pass

    print("\nExtracted Prices:", prices[:20])

    # Require only 3 prices
    assert len(prices) >= 3, f"Only found {len(prices)} prices!"

    # Check sorting of first few values
    first_vals = prices[:5]
    assert first_vals == sorted(first_vals), "Results are NOT sorted low → high!"
