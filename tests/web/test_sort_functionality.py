import pytest
from playwright.sync_api import sync_playwright
from utils.config import Config
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage

@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=Config.HEADLESS)
        yield browser
        browser.close()

def test_sort_by_price_high_to_low(browser):
    page = browser.new_page()
    page.goto(Config.HOME_URL)
    
    home_page = HomePage(page)
    home_page.search("Jacket")

    results_page = SearchResultsPage(page)
    results_page.sort_by("price")                 # select "Price" from dropdown
    results_page.set_sort_direction("desc")       # click descending icon

    prices = results_page.get_product_prices()
    assert prices == sorted(prices, reverse=True)


def test_sort_by_price_high_to_low(browser):
    page = browser.new_page()
    page.goto(Config.HOME_URL)
    
    home_page = HomePage(page)
    home_page.search("Jacket")

    results_page = SearchResultsPage(page)
    results_page.sort_by("price")                 # select "Price" from dropdown
    results_page.set_sort_direction("asc")       # click descending icon

    prices = results_page.get_product_prices()
    assert prices == sorted(prices, reverse=False)
