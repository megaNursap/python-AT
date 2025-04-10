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

def test_search_box_functionality(browser):
    page = browser.new_page()
    page.goto(Config.HOME_URL)

    home_page = HomePage(page)
    home_page.search("Jacket")

    results_page = SearchResultsPage(page)
    product_titles = results_page.get_product_titles()

    assert product_titles, "No search results found."
    assert all("jacket" in title.lower() for title in product_titles), "Not all results contain the word 'jacket'."