from playwright.sync_api import Page
from utils.config import Config

class SearchResultsPage:
    def __init__(self, page: Page):
        self.page = page
        self.product_titles_locator = "li.product-item .product-item-link"
        self.sort_dropdown = "select#sorter"
        self.product_prices_locator = "li.product-item .price"

    def get_product_titles(self):
        self.page.wait_for_selector(self.product_titles_locator)
        titles = self.page.locator(self.product_titles_locator).all_text_contents()
        return [title.strip() for title in titles]

    def sort_by(self, value: str = "price"):
        # Use JS to set the value and dispatch the change event
        self.page.evaluate(f'''
            () => {{
                const sorter = document.querySelector("#sorter");
                sorter.value = "{value}";
                sorter.dispatchEvent(new Event("change", {{ bubbles: true }}));
            }}
        ''')
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_timeout(2000)  # Optional: give time for UI to update

    def set_sort_direction(self, direction: str = "desc"):
        """
        direction: "asc" or "desc"
        """
        current_class = self.page.get_attribute("a.action.sorter-action", "class")

        if direction == "desc" and "sort-asc" in current_class:
            self.page.click("a.action.sorter-action")
            self.page.wait_for_load_state("networkidle")
        elif direction == "asc" and "sort-desc" in current_class:
            self.page.click("a.action.sorter-action")
            self.page.wait_for_load_state("networkidle")

        # Optional: small delay to ensure UI updates
        self.page.wait_for_timeout(2000)


    def get_product_prices(self):
        self.page.wait_for_selector(self.product_prices_locator)
        prices_text = self.page.locator(self.product_prices_locator).all_text_contents()

        prices = []
        for price_str in prices_text:
            try:
                cleaned = price_str.replace("$", "").replace(",", "").strip()
                prices.append(float(cleaned))
            except ValueError:
                continue

        return prices

    def click_first_product(self):
        self.page.wait_for_selector(self.product_titles_locator)
        self.page.locator(self.product_titles_locator).first.click()
