from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pytest

DRIVER_PATH = r"C:\chrome driver\chromedriver-win64\chromedriver.exe"

@pytest.fixture
def driver():
    options = Options()
    # Comment out the headless mode to see the browser
    # options.add_argument('--headless')
    options.add_argument('--disable-gpu')  # Required for certain environments
    service = Service(DRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()
