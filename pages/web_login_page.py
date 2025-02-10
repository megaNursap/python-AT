from utils.config import Config

class WebLoginPage:
    def __init__(self, page):
        self.page = page
        print("WebLoginPage initialized")

    def load(self):
        self.page.goto(Config.BASE_URL)

    def login(self, username, password):
        self.page.fill("#user-name", username)  # Faster than XPath
        self.page.fill("#password", password)
        self.page.click("#login-button[type='submit']")

