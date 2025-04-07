from pages import inventory_page
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.credentials import USERS, PASSWORD

import time

def test_single_purchase(driver, base_url):
    login_page = LoginPage(driver, base_url)
    login_page.perform_login(USERS["standard"], PASSWORD)
    inventory_page = InventoryPage(driver, base_url)
    inventory_page.add_to_cart_by_item_name("Sauce Labs Backpack")
    time.sleep(10)
