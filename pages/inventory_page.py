from selenium.webdriver.common.by import By

from .base_page import BasePage 


class InventoryPage(BasePage):
    PRODUCTS_HEADER = (By.CLASS_NAME, "title")
    
