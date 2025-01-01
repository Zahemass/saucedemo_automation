def test_cart_button_visibility(driver):
    driver.get("https://www.saucedemo.com/")  # Navigate to the URL
    driver.find_element("id", "user-name").send_keys("standard_user")
    driver.find_element("id", "password").send_keys("secret_sauce")
    driver.find_element("id", "login-button").click()

    cart_button = driver.find_element("id", "shopping_cart_container")
    assert cart_button.is_displayed(), "Cart button is not visible."
  
def test_add_multiple_items_to_cart(driver):
    # Step 1: Navigate to the website
    driver.get("https://www.saucedemo.com/")
    
    # Step 2: Login to the website
    driver.find_element("id", "user-name").send_keys("standard_user")
    driver.find_element("id", "password").send_keys("secret_sauce")
    driver.find_element("id", "login-button").click()

    # Step 3: Add multiple items to the cart
    driver.find_element("id", "add-to-cart-sauce-labs-backpack").click()
    driver.find_element("id", "add-to-cart-sauce-labs-bike-light").click()

    # Step 4: Verify the cart badge shows "2"
    cart_badge = driver.find_element("class name", "shopping_cart_badge")
    assert cart_badge.text == "2", "Failed to add multiple items to the cart."
    
