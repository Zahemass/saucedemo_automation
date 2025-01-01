import pytest
from selenium import webdriver
from utils.config import BASE_URL, DRIVER_PATH
from pages.login_page import LoginPage
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    service = Service(DRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


def test_login_standard_user(driver):
    driver.get(BASE_URL)
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    assert "inventory" in driver.current_url
    print("login testing completed successfully.")