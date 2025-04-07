from pages.base_page import BasePage

from selenium.webdriver.common.by import By
import re

class CheckoutStepTwoPage:
    SUBTOTAL_LABEL = (By.CLASS_NAME, "summary_subtotal_label")
    SUMMARY_TAX_LABEL = (By.CLASS_NAME, "summary_tax_label")
    SUMMARY_TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")

    def get_subtotal(self):
        text = self.find(self.SUBTOTAL_LABEL).text
        value = re.search(r"\$([0-9]+\.[0-9]{2})", text)
        return float(match.group(1)) if match else None

    
    
