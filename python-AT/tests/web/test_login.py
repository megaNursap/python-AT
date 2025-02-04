import pytest
from playwright.sync_api import sync_playwright
from pages.web_login_page import WebLoginPage

@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()

def test_valid_login(browser):
    page = browser.new_page()
    login_page = WebLoginPage(page)
    login_page.load()
    login_page.login("testuser", "password123")
    assert "Dashboard" in page.title()
