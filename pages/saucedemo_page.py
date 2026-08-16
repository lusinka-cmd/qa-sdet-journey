from playwright.sync_api import Page, expect


class SauceDemoLoginPage:
    URL = "https://www.saucedemo.com/"

    def __init__(self, page: Page):
        self.page = page
        self.username = page.locator('[data-test="username"]')
        self.password = page.locator('[data-test="password"]')
        self.login_button = page.locator('[data-test="login-button"]')
        self.error_message = page.locator('[data-test="error"]')

    def open(self) -> None:
        self.page.goto(self.URL, wait_until="domcontentloaded")
        expect(self.login_button).to_be_visible()

    def login(self, username: str, password: str) -> None:
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()

    def verify_inventory_is_displayed(self) -> None:
        expect(self.page).to_have_url(f"{self.URL}inventory.html")
        expect(self.page.locator('[data-test="inventory-container"]')).to_be_visible()

    def verify_login_error(self) -> None:
        expect(self.error_message).to_be_visible()
        expect(self.error_message).to_contain_text("Username and password do not match")
