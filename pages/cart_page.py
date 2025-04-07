from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    CART_ITEM = (By.CLASS_NAME, "cart_item")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def get_cart_items_number(self):
        return len(self.find_multiple(self.CART_ITEM))

    def go_to_checkout(self):
        self.click(self.CHECKOUT_BUTTON)
