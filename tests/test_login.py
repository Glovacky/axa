from pages import inventory_page
from utils.credentials import USERS, PASSWORD
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_login_standard_user(driver, base_url):
    login_page = LoginPage(driver, base_url)
    login_page.perform_login(USERS["standard"], PASSWORD)
    inventory_page = InventoryPage(driver, base_url)
     
    assert inventory_page.is_on_inventory_page(), "Should be redirected to inventory page"


def test_login_locked_out_user(driver, base_url):
    login_page = LoginPage(driver, base_url)
    login_page.perform_login(USERS["locked_out"], PASSWORD)

    assert driver.current_url == base_url, "Locked out user should not be redirected"
    assert login_page.check_locked_out(), "Error message for locked out user should show up"


def test_login_wrong_creds(driver, base_url):
    login_page = LoginPage(driver, base_url)
    login_page.perform_login("wrong","wrong")
    assert driver.current_url == base_url, "Wrong credentials should not redirect"
    assert login_page.check_wrong_creds(),"Error message for wrong credentials should show up"

