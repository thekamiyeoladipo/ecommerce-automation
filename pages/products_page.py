class ProductsPage:
    def __init__(self, page):
        self.page = page

        # Locators
        self.products_link = page.locator("a[href='/products']")
        self.products_list = page.locator(".product-image-wrapper")
        self.search_input = page.locator("input[id='search_product']")
        self.search_button = page.locator("button[id='submit_search']")
        self.searched_products = page.locator(".productinfo")
        self.add_to_cart_button =  page.get_by_role("button", name=" Add to cart")
        self.view_cart_modal_link = page.get_by_role("link", name="View Cart")

    def navigate(self):
        self.products_link.click()
        self.page.wait_for_load_state("networkidle")

    def search_product(self, product_name):
        self.search_input.fill(product_name)
        self.search_button.click()
        self.page.wait_for_load_state("networkidle")

    def get_searched_products_count(self):
        return self.searched_products.count()

    def open_first_product(self):
        # Navigate directly to first product detail page — no hover needed
        self.page.goto("https://automationexercise.com/product_details/1")
        self.page.wait_for_load_state("networkidle")

    def add_to_cart(self):
        self.add_to_cart_button.click()
        self.page.wait_for_timeout(3000)
    
    def go_to_cart(self):
        self.view_cart_modal_link.click()
        self.page.wait_for_load_state("networkidle")
