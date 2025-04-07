import re

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutStepTwoPage(BasePage):
    SUBTOTAL_LABEL = (By.CLASS_NAME, "summary_subtotal_label")
    SUMMARY_TAX_LABEL = (By.CLASS_NAME, "summary_tax_label")
    SUMMARY_TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")

    def _extract_price_from_label(self, locator):
        text = self.get_text(locator)
        match = re.search(r"\$([0-9]+\.[0-9]{2})", text)
        return float(match.group(1)) if match else None

    def get_subtotal(self):
        return self._extract_price_from_label(self.SUBTOTAL_LABEL)

    def get_tax(self):
        return self._extract_price_from_label(self.SUMMARY_TAX_LABEL)

    def get_total(self):
        return self._extract_price_from_label(self.SUMMARY_TOTAL_LABEL)
