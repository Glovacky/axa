from utils.credentials import USERS, PASSWORD
from pages.login_page import LoginPage
from utils.assertions import check_logged_in

def test_login_standard_user(driver):
    login_page = LoginPage(driver)
    login_page.open_url("https://www.saucedemo.com/")
    login_page.perform_login(USERS["standard"], PASSWORD)
    assert check_logged_in(driver), "Login was not succesful"
