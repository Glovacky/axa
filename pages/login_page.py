from selenium.webdriver.common.by import By

from base_page import BasePage

class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def perform_login(self, username, password):
        self.fill_input(self.USERNAME_INPUT, username)
        self.fill_input(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)



