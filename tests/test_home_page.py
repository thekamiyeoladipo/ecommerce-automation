from pages.home_page import HomePage

class TestHomePage:

    def test_home_page_loads(self, page, base_url):
        home = HomePage(page)
        home.navigate()
        assert home.is_logo_visible(), "Home page logo should be visible"

    def test_navigate_to_login(self, page, base_url):
        home = HomePage(page)
        home.navigate()
        home.go_to_login()
        assert "login" in page.url, "Should navigate to login page"