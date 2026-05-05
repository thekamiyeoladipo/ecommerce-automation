class CartPage:
    def __init__(self, page):
        self.page = page

        # Locators
        self.cart_items = page.locator("tr.cart_item")
        self.cart_link = page.locator("a[href='/view_cart']")
        self.remove_button = page.locator("a.cart_quantity_delete").first
        self.empty_cart_message = page.locator("b:has-text('Cart is empty!')")
        self.proceed_to_checkout = page.locator("a:has-text('Proceed To Checkout')")

    def navigate(self):
        self.cart_link.click()
        self.page.wait_for_load_state("networkidle")

    def get_cart_items_count(self):
        return self.cart_items.count()

    def is_cart_empty(self):
        try:
            self.empty_cart_message.wait_for(state="visible", timeout=5000)
            return True
        except:
            return False

    def remove_first_item(self):
        self.remove_button.click()
        self.page.wait_for_timeout(2000)

    def proceed_to_checkout(self):
        self.proceed_to_checkout.click()
        self.page.wait_for_load_state("networkidle")