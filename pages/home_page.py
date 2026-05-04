class HomePage:
    def __init__(self, page):
        self.page = page
        self.url = "https://automationexercise.com"

        # Locators
        self.logo = page.locator("img[alt='Website for automation practice']")
        self.signup_login_link = page.locator("a[href='/login']")

    def navigate(self):
        self.page.goto(self.url)

    def is_logo_visible(self):
        return self.logo.is_visible()

    def go_to_login(self):
        self.signup_login_link.click()