from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


class TestProductsAndCart:

    def test_products_page_loads(self, page, base_url):
        home = HomePage(page)
        home.navigate()

        products = ProductsPage(page)
        products.navigate()

        assert "products" in page.url, "Should navigate to products page"

    def test_all_products_are_visible(self, page, base_url):
        home = HomePage(page)
        home.navigate()

        products = ProductsPage(page)
        products.navigate()

        assert products.products_list.count() > 0, "Products list should not be empty"

    def test_search_product(self, page, base_url):
        home = HomePage(page)
        home.navigate()

        products = ProductsPage(page)
        products.navigate()
        products.search_product("T-Shirt")

        count = products.get_searched_products_count()
        assert count > 0, "Search results should return at least one product"

    def test_add_product_to_cart(self, page, base_url):
        home = HomePage(page)
        home.navigate()

        products = ProductsPage(page)
        products.navigate()
        products.add_first_product_to_cart()
        products.continue_shopping()
        products.go_to_cart()

        cart = CartPage(page)
        assert cart.get_cart_items_count() > 0, "Cart should have at least one item after adding"

    def test_remove_product_from_cart(self, page, base_url):
        home = HomePage(page)
        home.navigate()

        products = ProductsPage(page)
        products.navigate()
        products.add_first_product_to_cart()
        products.continue_shopping()
        products.go_to_cart()

        cart = CartPage(page)
        cart.remove_first_item()

        assert cart.is_cart_empty(), "Cart should be empty after removing the only item"

    def test_cart_persists_after_login(self, page, base_url, test_email, test_password):
        # Add item to cart as guest
        home = HomePage(page)
        home.navigate()

        products = ProductsPage(page)
        products.navigate()
        products.add_first_product_to_cart()
        products.continue_shopping()

        # Login
        home.go_to_login()
        login = LoginPage(page)
        login.login(test_email, test_password)
        assert login.is_logged_in(), "User should be logged in"

        # Check cart still has item
        cart = CartPage(page)
        cart.navigate()
        assert cart.get_cart_items_count() > 0, "Cart should persist items after login"