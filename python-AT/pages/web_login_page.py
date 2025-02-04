class WebLoginPage:
    def __init__(self, page):
        self.page = page

    def load(self):
        self.page.goto("https://example.com/login")

    def login(self, username, password):
        self.page.fill("input[name='username']", username)
        self.page.fill("input[name='password']", password)
        self.page.click("button[type='submit']")
