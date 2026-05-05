from pages.home_page import HomePage
from pages.login_page import LoginPage

class TestLogin:

    def test_valid_login(self, page, base_url, test_email, test_password):
        home = HomePage(page)
        home.navigate()
        home.go_to_login()

        login = LoginPage(page)
        login.login(test_email, test_password)

        assert login.is_logged_in(), "User should be logged in with valid credentials"

    def test_invalid_login_wrong_password(self, page, base_url, test_email):
        home = HomePage(page)
        home.navigate()
        home.go_to_login()

        login = LoginPage(page)
        login.login(test_email, "wrongpassword123")

        assert login.is_error_visible(), "Error message should appear with wrong password"

    def test_invalid_login_wrong_email(self, page, base_url):
        home = HomePage(page)
        home.navigate()
        home.go_to_login()

        login = LoginPage(page)
        login.login("notareal@email.com", "somepassword123")

        assert login.is_error_visible(), "Error message should appear with unregistered email"

    def test_logout(self, page, base_url, test_email, test_password):
        home = HomePage(page)
        home.navigate()
        home.go_to_login()

        login = LoginPage(page)
        login.login(test_email, test_password)
        assert login.is_logged_in(), "User should be logged in before logout test"

        login.logout()
        assert "login" in page.url, "User should be redirected to login page after logout"