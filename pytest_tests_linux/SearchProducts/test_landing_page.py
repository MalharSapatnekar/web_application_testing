import pytest
from selenium.webdriver.common.by import By

@pytest.mark.tc_id("TC-PYT-007")
def test_user_can_open_amazon(browser):
    browser.get("https://www.amazon.com")
    assert "Amazon" in browser.title
