from pages.cart_page import CartPage
from pages.checkout1 import CheckoutStepOnePage
from pages.checkout2 import CheckoutStepTwoPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.credentials import PASSWORD, USERS


def test_single_purchase(driver, base_url):
    login_page = LoginPage(driver, base_url)
    login_page.perform_login(USERS["standard"], PASSWORD)

    inventory_page = InventoryPage(driver, base_url)
    inventory_page.add_to_cart_by_item_name("Sauce Labs Backpack")
    inventory_page.open_cart()

    cart_page = CartPage(driver, base_url)
    assert cart_page.get_cart_items_number() == 1, "Should be 1 item in the cart"
    cart_page.go_to_checkout()

    checkout1 = CheckoutStepOnePage(driver, base_url)
    checkout1.complete_checkout_details("Jan", "Kowalski", "11-111")

    checkout2 = CheckoutStepTwoPage(driver, base_url)
    subtotal = checkout2.get_subtotal()
    tax = checkout2.get_tax()
    total = checkout2.get_total()

    assert subtotal == 29.99, "Subtotal is wrong value"
    assert tax == 2.4, "Tax is wrong value"
    assert total == 32.39, "Total is wrong value"
    assert total == subtotal + tax, "Tax + subtotal is different than total"
