import pytest
from selenium import webdriver
from utils.helpers import load_json

from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--incognito")
    
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(1)
    
    yield driver

    driver.quit()


@pytest.fixture(scope="function")
def base_url(file="config.json"):
    data = load_json(file)
    return data["base_url"]
    
