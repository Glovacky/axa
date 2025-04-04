from utils.credentials import USERS, PASSWORD
from pages.login_page import LoginPage

def test_login_standard_user(driver):
    login_page = LoginPage(driver)
    login_page.open("https://www.saucedemo.com/")
    login_page.login(USERS["standard"], PASSWORD)
    # assertions here...
