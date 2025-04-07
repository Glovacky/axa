from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


class BasePage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url


    def open_url(self, url):
        self.driver.get(url)


    def find(self, locator):
        return self.driver.find_element(*locator)
    
    
    def find_multiple(self, locator):
        return self.driver.find_elements(*locator)


    def click(self, locator):
        self.find(locator).click()
        time.sleep(1)


    def fill_input(self, locator, text):
        self.find(locator).send_keys(text)


    def get_text(self, locator):
        return self.find(locator).text
    
    
    def check_element_exists(self, element_locator, timeout=1):
        
        #print("checking existence of an element:")
        #print(element_locator)
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(element_locator)
            )
            #print("found.")
            return True
        except Exception as e:
            #print(f"not found, error: {e}")
            return False    
