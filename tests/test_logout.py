from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_logout(driver):
    driver.get("https://www.saucedemo.com/")  # Navigate to the URL

    # Login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Open the hamburger menu
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "react-burger-menu-btn"))
    ).click()

    # Wait for the logout link to be visible and click it
    logout_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
    )
    logout_link.click()

    # Validate redirection to the login page
    assert driver.current_url == "https://www.saucedemo.com/", "Logout failed or URL mismatch."
    print("logout testing completed successfully.")
