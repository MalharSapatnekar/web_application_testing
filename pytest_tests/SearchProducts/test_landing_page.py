from selenium.webdriver.common.by import By

def test_user_can_open_amazon(browser):
    browser.get("https://www.amazon.com")
    assert "Amazon" in browser.title
