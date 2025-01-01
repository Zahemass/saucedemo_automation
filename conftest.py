from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pytest

DRIVER_PATH = r" " # your chrome driver path

@pytest.fixture
def driver():
    options = Options()
    options.add_argument('--disable-gpu') 
    service = Service(DRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()
