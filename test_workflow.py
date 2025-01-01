import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import random

# Path to your chromedriver
DRIVER_PATH = r" " # your chrome driver path

# Driver fixture
def setup_driver():
    options = Options()
    options.add_argument("--disable-gpu")
    service = Service(DRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=options)
    return driver


# Test function
def test_automation_workflow():
    driver = setup_driver()
    
    try:
        driver.get("https://www.saucedemo.com/")
        time.sleep(2)  # Observe the login page

        
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)  # Observe the product page

        
        product_buttons = driver.find_elements(By.CLASS_NAME, "btn_inventory")
        selected_products = random.sample(product_buttons, 4)
        for product in selected_products:
            product.click()
            time.sleep(1)  # Observe each product addition

       
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        time.sleep(2)  # Observe the cart page

        
        cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
        assert len(cart_items) == 4, f"Expected 4 items in the cart, but found {len(cart_items)}."
        print("add random products verification test")

       
        driver.find_element(By.ID, "react-burger-menu-btn").click()
        time.sleep(1)  # Observe the menu opening
        driver.find_element(By.ID, "logout_sidebar_link").click()
        time.sleep(2)  # Observe the logout process

    finally:
        driver.quit()


# Execute the test
if __name__ == "__main__":
    test_automation_workflow()
