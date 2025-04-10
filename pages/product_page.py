from playwright.sync_api import Page

class ProductPage:
    def __init__(self, page: Page):
        self.page = page
        self.size_option = "div.swatch-attribute.size div.swatch-option"
        self.color_option = "div.swatch-attribute.color div.swatch-option"
        self.add_to_cart_button = "button#product-addtocart-button"
        self.success_message = "div.message-success div"

    def select_size(self):
        self.page.locator(self.size_option).first.click()

    def select_color(self):
        self.page.locator(self.color_option).first.click()

    def add_to_cart(self):
        self.page.click(self.add_to_cart_button)

    def get_success_message(self):
        self.page.wait_for_selector(self.success_message)
        return self.page.locator(self.success_message).inner_text()
