from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def open_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    def get_cart_items(self):
        cart_elements = self.driver.find_elements(By.CLASS_NAME, "cart_item")
        cart_items = []
        for item in cart_elements:
            name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
            price = item.find_element(By.CLASS_NAME, "inventory_item_price").text
            cart_items.append({"name": name, "price": price})
        return cart_items
