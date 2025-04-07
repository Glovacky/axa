from selenium.webdriver.common.by import By

from .base_page import BasePage 


class InventoryPage(BasePage):
    PRODUCTS_HEADER = (By.CLASS_NAME, "title")

    
    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        self.inventory_url = f"{base_url}inventory.html"


    def check_access_inventory(self):
        return self.check_element_exists(self.PRODUCTS_HEADER)

    
    def is_on_inventory_page(self):
        return self.inventory_url == self.driver.current_url
