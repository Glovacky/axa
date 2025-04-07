from selenium.webdriver.common.by import By

from .base_page import BasePage


class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_HEADER_PATTERN = (
        "//h3[contains(@data-test,'error') and contains(text(),'%s')]"
    )

    def get_locator_error_wrong_creds(self):
        return (
            By.XPATH,
            self.ERROR_HEADER_PATTERN
            % "Epic sadface: Username and password do not match any user in this service",
        )

    def get_locator_error_locked_out(self):
        return (
            By.XPATH,
            self.ERROR_HEADER_PATTERN
            % "Epic sadface: Sorry, this user has been locked out.",
        )

    def perform_login(self, username, password):
        self.open_url(self.base_url)
        self.fill_input(self.USERNAME_INPUT, username)
        self.fill_input(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def check_wrong_creds(self):
        error_loc = self.get_locator_error_wrong_creds()
        return self.check_element_exists(error_loc)

    def check_locked_out(self):
        error_loc = self.get_locator_error_locked_out()
        return self.check_element_exists(error_loc)
