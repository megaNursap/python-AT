from utils.config import Config

class HomePage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto(Config.HOME_URL)

    def search(self, item_name: str):
        print("Searching for item:", item_name)
        self.page.fill("#search", item_name)
        self.page.press("#search", "Enter")  # Important: this submits the search
        self.page.wait_for_load_state("networkidle")  # Ensures results load