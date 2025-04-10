class Config:
    BASE_URL = "https://www.saucedemo.com"
    HOME_URL = "https://magento.softwaretestingboard.com/"
    API_URL = "https://jsonplaceholder.typicode.com"
    USERNAME = "testuser"
    PASSWORD = "password123"
    MOBILE_APP_PATH = "/path/to/app.apk"

    # WebDriver settings
    BROWSER = "chrome"
    HEADLESS = False

    # Timeout settings
    SHORT_WAIT = 3
    MEDIUM_WAIT = 5
    LONG_WAIT = 10

    # HTTP Status Codes
    STATUS_OK = 200
    STATUS_CREATED = 201
    STATUS_NOT_FOUND = 404