from selenium.webdriver.common.by import By
import random

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def is_cart_button_visible(self):
        return self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").is_displayed()

    def get_products(self):
        product_elements = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        products = []
        for product in product_elements:
            name = product.find_element(By.CLASS_NAME, "inventory_item_name").text
            price = product.find_element(By.CLASS_NAME, "inventory_item_price").text
            products.append({"name": name, "price": price})
        return products

    def get_random_products(self, count):
        products = self.get_products()
        return random.sample(products, count)

    def add_product_to_cart(self, product_name):
        products = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        for product in products:
            if product_name in product.text:
                product.find_element(By.CLASS_NAME, "btn_inventory").click()
                break

    def get_cart_count(self):
        return int(self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text)
