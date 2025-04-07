from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from .base_page import BasePage


class InventoryPage(BasePage):
    PRODUCTS_HEADER = (By.CLASS_NAME, "title")
    CART_BUTTON_BY_PROD_NAME_PATTERN = f"//div[contains(@class,'inventory_item_name') and contains(text(),'%s')]//ancestor::div[contains(@class,'inventory_item_description')]//button"
    OPEN_CART_BUTTON = (By.CLASS_NAME, "shopping_cart_link")
    PRODUCT_NAME_LOCATORS = (By.CLASS_NAME, "inventory_item_name")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    PRODUCT_PRICE_LOCATOR = (By.CLASS_NAME, "inventory_item_price")

    def select_sort_option(self, value: str):
        """
        value must be one of: "az", "za", "lohi", "hilo"
        """
        dropdown = Select(self.find(self.SORT_DROPDOWN))
        dropdown.select_by_value(value)

    def get_product_prices(self):
        elements = self.find_multiple(self.PRODUCT_PRICE_LOCATOR)
        return [float(el.text.strip().replace("$", "")) for el in elements]

    def is_sorted_by_price(self, descending=False):
        prices = self.get_product_prices()
        return prices == sorted(prices, reverse=descending)

    def get_product_names(self):
        elements = self.find_multiple(self.PRODUCT_NAME_LOCATORS)
        return [el.text.strip() for el in elements]

    def is_sorted_alphabetically(self, descending=False):
        names = self.get_product_names()
        sorted_names = sorted(names, reverse=descending)
        return names == sorted_names

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        self.inventory_url = f"{base_url}inventory.html"

    def check_access_inventory(self):
        return self.check_element_exists(self.PRODUCTS_HEADER)

    def is_on_inventory_page(self):
        return self.inventory_url == self.driver.current_url

    def add_to_cart_by_item_name(self, product_name):
        xpath = self.CART_BUTTON_BY_PROD_NAME_PATTERN % product_name
        self.find((By.XPATH, xpath)).click()

    def open_cart(self):
        self.find(self.OPEN_CART_BUTTON).click()
