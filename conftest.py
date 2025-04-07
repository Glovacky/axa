import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils.helpers import load_json


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


@pytest.fixture(scope="session")
def config():
    return load_json("config.json")


@pytest.fixture(scope="function")
def base_url(config):
    return config["base_url"]


@pytest.fixture(scope="function")
def users(config):
    return config["users"]


@pytest.fixture(scope="function")
def password(config):
    return config["password"]
