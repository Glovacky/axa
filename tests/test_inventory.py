from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_sorting_by_name(driver, base_url, users, password):
    login_page = LoginPage(driver, base_url)
    login_page.perform_login(users["standard"], password)

    inventory_page = InventoryPage(driver, base_url)

    inventory_page.select_sort_option("az")
    assert (
        inventory_page.is_sorted_alphabetically()
    ), "Products should be sorted alphabetically ascending"

    inventory_page.select_sort_option("za")
    assert inventory_page.is_sorted_alphabetically(
        descending=True
    ), "Products should be sorted alphabetically descending"


def test_sorting_by_price(driver, base_url, users, password):
    login_page = LoginPage(driver, base_url)
    login_page.perform_login(users["standard"], password)

    inventory_page = InventoryPage(driver, base_url)

    inventory_page.select_sort_option("lohi")
    assert inventory_page.is_sorted_by_price(), "Prices should be sorted low to high"

    inventory_page.select_sort_option("hilo")
    assert inventory_page.is_sorted_by_price(
        descending=True
    ), "Prices should be sorted high to low"
