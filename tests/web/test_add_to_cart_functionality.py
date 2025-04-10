import pytest
from playwright.sync_api import sync_playwright
from utils.config import Config
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=Config.HEADLESS)
        yield browser
        browser.close()

def test_add_to_cart(browser):
    page = browser.new_page()
    page.goto(Config.HOME_URL)

    home_page = HomePage(page)
    home_page.search("Jacket")

    results_page = SearchResultsPage(page)
    results_page.click_first_product()

    # product_page = ProductPage(page)
    # product_page.select_size()
    # product_page.select_color()
    # product_page.add_to_cart()

    # assert product_page.get_success_message() is True

    # product_page.go_to_cart()

    # cart_page = CartPage(page)
    # assert cart_page.verify_selected_size_color()
    
    # cart_page.update_quantity(2)
    # assert cart_page.verify_subtotal_updated(2)
