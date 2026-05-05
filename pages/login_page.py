class LoginPage:
    def __init__(self, page):
        self.page = page

        # Locators
        self.login_email = page.locator("input[data-qa='login-email']")
        self.login_password = page.locator("input[data-qa='login-password']")
        self.login_button = page.locator("button[data-qa='login-button']")
        self.error_message = page.locator("p:has-text('Your email or password is incorrect!')")
        self.logged_in_username = page.locator("a:has-text('Logged in as')")
        self.logout_button = page.locator("a[href='/logout']")

    def login(self, email, password):
        self.login_email.fill(email)
        self.login_password.fill(password)
        self.login_button.click()
        # Wait for page to finish navigating after login
        self.page.wait_for_load_state("networkidle")

    def is_logged_in(self):
        try:
            self.logged_in_username.wait_for(state="visible", timeout=8000)
            return True
        except:
            return False

    def is_error_visible(self):
        try:
            self.error_message.wait_for(state="visible", timeout=5000)
            return True
        except:
            return False

    def logout(self):
        self.logout_button.click()
        self.page.wait_for_load_state("networkidle")