from selenium.common.exceptions import NoSuchElementException

from pages.base_page import BasePage
from pages.inventory_page import InventoryPage


def check_logged_in(driver):
    driver.get("https://www.saucedemo.com/inventory.html")
    
    try:
        driver.find_element(*InventoryPage.PRODUCTS_HEADER)
    except NoSuchElementException:
        return False
    else:
        return True
