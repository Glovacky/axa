from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutStepOnePage(BasePage):
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    ZIP_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")

    def complete_checkout_details(self, first_name, last_name, postal_code):
        self.fill_input(self.FIRST_NAME_INPUT, first_name)
        self.fill_input(self.LAST_NAME_INPUT, last_name)
        self.fill_input(self.ZIP_INPUT, postal_code)
        self.click(self.CONTINUE_BUTTON)
