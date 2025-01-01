import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    
    screenshots_dir = os.path.join(os.getcwd(), "screenshots")
    if not os.path.exists(screenshots_dir):
        os.makedirs(screenshots_dir)

def test_verify_cart(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    
    product_buttons = driver.find_elements(By.CLASS_NAME, "btn_inventory")
    for i in range(4):
        product_buttons[i].click()
    
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    
   
    cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(cart_items) == 4, "Cart does not contain 4 products"
    for item in cart_items:
        product_name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
        product_price = item.find_element(By.CLASS_NAME, "inventory_item_price").text
        print(f"Product Name: {product_name}, Price: {product_price}")

def test_checkout_process(driver, request):
    screenshots_dir = os.path.join(os.getcwd(), "screenshots")
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
   
    product_buttons = driver.find_elements(By.CLASS_NAME, "btn_inventory")
    for i in range(4):
        product_buttons[i].click()
    
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver.find_element(By.ID, "checkout").click()
    driver.find_element(By.ID, "first-name").send_keys("John")
    driver.find_element(By.ID, "last-name").send_keys("Doe")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.ID, "continue").click()
    
    
    screenshot_path = os.path.join(screenshots_dir, "checkout_overview.png")
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved at: {screenshot_path}")
    
    
    if hasattr(request.node, "add_report_section"):
        with open(screenshot_path, "rb") as image_file:
            request.node.add_report_section("call", "image", f"Checkout screenshot: {screenshot_path}")
    
    
    cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(cart_items) == 4, "Checkout does not contain 4 products"
    for item in cart_items:
        product_name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
        product_price = item.find_element(By.CLASS_NAME, "inventory_item_price").text
        print(f"Product Name: {product_name}, Price: {product_price}")
    
   
    driver.find_element(By.ID, "finish").click()
    confirmation_message = driver.find_element(By.CLASS_NAME, "complete-header").text
    assert confirmation_message.lower() == "thank you for your order!".lower(), "Checkout not completed successfully"
    print("Test Case 8: Checkout completed successfully.")
