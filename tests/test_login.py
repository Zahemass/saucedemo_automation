import pytest
from selenium import webdriver
from utils.config import BASE_URL, DRIVER_PATH
from pages.login_page import LoginPage
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    service = Service(DRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

@pytest.mark.parametrize("username", [
    "standard_user", 
    "problem_user", 
    "performance_glitch_user", 
    "locked_out_user"
])
def test_login_various_users(driver, username):
    driver.get(BASE_URL)
    login_page = LoginPage(driver)
    login_page.login(username, "secret_sauce")
    if username == "locked_out_user":
        error_message = driver.find_element(By.CLASS_NAME, "error-message-container").text
        assert "locked out" in error_message.lower()
    else:
        assert "inventory" in driver.current_url
        print(username,"Successfully logged")

def test_login_using_cookies(driver):
    driver.get(BASE_URL)
    driver.add_cookie({"name": "session-id", "value": "mock-session-id", "path": "/"})
    driver.refresh()
    assert "inventory" in driver.current_url 

