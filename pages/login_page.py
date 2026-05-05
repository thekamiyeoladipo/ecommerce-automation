class LoginPage:
    def __init__(self, page):
        self.page = page

        # Locators
        self.login_email = page.locator("input[data-qa='login-email']")
        self.login_password = page.locator("input[data-qa='login-password']")
        self.login_button = page.locator("button[data-qa='login-button']")
        self.error_message = page.locator("p:has-text('Your email or password is incorrect!')")
        self.logged_in_username = page.locator("a:has-text(' Logged in as')")
        self.logout_button = page.locator("a[href='/logout']")

    def login(self, email, password):
        self.login_email.fill(email)
        self.login_password.fill(password)
        self.login_button.click()

    def is_logged_in(self):
        return self.logged_in_username.is_visible()

    def is_error_visible(self):
        return self.error_message.is_visible()

    def logout(self):
        self.logout_button.click()