from selenium.webdriver.common.by import By

from .base_page import BasePage


class CheckoutCompletePage(BasePage):
    THANK_YOU_HEADER = (By.CLASS_NAME, "complete-header")

    def thank_you_header_visible(self):
        return self.check_element_exists(self.THANK_YOU_HEADER)
