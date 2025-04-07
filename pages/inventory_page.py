from selenium.webdriver.common.by import By

from .base_page import BasePage 


class InventoryPage(BasePage):
    PRODUCTS_HEADER = (By.CLASS_NAME, "title")
    CART_BUTTON_BY_PROD_NAME_PATTERN = f"//div[contains(@class,'inventory_item_name') and contains(text(),'%s')]//ancestor::div[contains(@class,'inventory_item_description')]//button"
    OPEN_CART_BUTTON = (By.CLASS_NAME, "shopping_cart_link") 

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
        
    
