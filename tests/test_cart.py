def test_cart_button_visibility(driver):
    driver.get("https://www.saucedemo.com/")  
    driver.find_element("id", "user-name").send_keys("standard_user")
    driver.find_element("id", "password").send_keys("secret_sauce")
    driver.find_element("id", "login-button").click()

    cart_button = driver.find_element("id", "shopping_cart_container")
    assert cart_button.is_displayed(), "Cart button is not visible."
    print("Button Visibility is completed")
  
def test_add_multiple_items_to_cart(driver):
   
    driver.get("https://www.saucedemo.com/")
    
  
    driver.find_element("id", "user-name").send_keys("standard_user")
    driver.find_element("id", "password").send_keys("secret_sauce")
    driver.find_element("id", "login-button").click()

   
    driver.find_element("id", "add-to-cart-sauce-labs-backpack").click()
    driver.find_element("id", "add-to-cart-sauce-labs-bike-light").click()

   
    cart_badge = driver.find_element("class name", "shopping_cart_badge")
    assert cart_badge.text == "2", "Failed to add multiple items to the cart."
    print("Multiple product adding test completed")
    
