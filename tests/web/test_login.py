import pytest
from playwright.sync_api import sync_playwright
from pages.web_login_page import WebLoginPage
from utils.config import Config
from utils.test_data import TestData

@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=Config.HEADLESS)
        yield browser
        browser.close()

def test_valid_login(browser):
    page = browser.new_page()
    login_page = WebLoginPage(page)
    login_page.load()
    user = TestData.test_users["standard_user"]
    login_page.login(user['username'], user['password'])
    assert "Swag Labs" in page.title()
