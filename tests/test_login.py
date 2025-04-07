import pytest

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@pytest.mark.parametrize(
    "username, password, should_redirect, expected_error",
    [
        ("standard_user", "secret_sauce", True, None),  # valid user
        ("locked_out_user", "secret_sauce", False, "locked_out"),  # locked out user
        ("wrong", "wrong", False, "wrong_creds"),  # invalid user
    ],
)
def test_login_cases(
    driver, base_url, username, password, should_redirect, expected_error
):
    login_page = LoginPage(driver, base_url)
    login_page.perform_login(username, password)

    if should_redirect:
        inventory_page = InventoryPage(driver, base_url)
        assert (
            inventory_page.is_on_inventory_page()
        ), f"{username} should be redirected to inventory page"
    else:
        assert driver.current_url == base_url, f"{username} should not be redirected"

        if expected_error == "locked_out":
            assert login_page.check_locked_out(), "Locked out user error should show up"
        elif expected_error == "wrong_creds":
            assert (
                login_page.check_wrong_creds()
            ), "Wrong credentials error should show up"
