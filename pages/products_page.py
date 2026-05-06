class ProductsPage:
    def __init__(self, page):
        self.page = page

        # Locators
        self.products_link = page.locator("a[href='/products']")
        self.products_list = page.locator(".product-image-wrapper")
        self.search_input = page.locator("input[id='search_product']")
        self.search_button = page.locator("button[id='submit_search']")
        self.searched_products = page.locator(".productinfo")
        self.first_product = page.locator(".product-image-wrapper").first
        self.first_add_to_cart = page.locator(".product-overlay .add-to-cart").first
        self.continue_shopping_button = page.locator("button:has-text('Continue Shopping')")
        self.view_cart_link = page.locator("a.view-cart")

    def navigate(self):
        self.products_link.click()
        self.page.wait_for_load_state("networkidle")

    def search_product(self, product_name):
        self.search_input.fill(product_name)
        self.search_button.click()
        self.page.wait_for_load_state("networkidle")

    def get_searched_products_count(self):
        return self.searched_products.count()

    def add_first_product_to_cart(self):
        # Hover to reveal the hidden overlay button first
        self.first_product.hover()
        self.page.wait_for_timeout(800)
        self.first_add_to_cart.click()
        self.page.wait_for_load_state("networkidle")

    def continue_shopping(self):
        self.continue_shopping_button.click()
        self.page.wait_for_timeout(500)

    def go_to_cart(self):
        self.view_cart_link.click()
        self.page.wait_for_load_state("networkidle")