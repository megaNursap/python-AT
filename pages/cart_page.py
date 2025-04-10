from playwright.sync_api import Page

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_icon = "a.showcart"
        self.view_edit_cart_link = "a[href$='/checkout/cart/']"
        self.size_locator = "dd[data-th='Size']"
        self.color_locator = "dd[data-th='Color']"
        self.qty_input = "input.input-text.qty"
        self.update_button = "button.update"
        self.subtotal_locator = "td.subtotal .price"

    def open_cart(self):
        self.page.click(self.cart_icon)
        self.page.wait_for_selector(self.view_edit_cart_link)
        self.page.click(self.view_edit_cart_link)
        self.page.wait_for_url("**/checkout/cart/")

    def get_selected_size(self):
        return self.page.locator(self.size_locator).inner_text()

    def get_selected_color(self):
        return self.page.locator(self.color_locator).inner_text()

    def update_quantity(self, qty: int):
        self.page.fill(self.qty_input, str(qty))
        self.page.click(self.update_button)
        self.page.wait_for_timeout(2000)  # Give it time to recalculate subtotal

    def get_subtotal(self):
        subtotal_text = self.page.locator(self.subtotal_locator).inner_text()
        return float(subtotal_text.replace("$", "").replace(",", "").strip())
