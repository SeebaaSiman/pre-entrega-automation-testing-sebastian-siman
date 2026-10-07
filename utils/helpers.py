from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login_standard_user(driver):
    """
    Navega a saucedemo e inicia sesión con el usuario estándar.
    """
    driver.get("https://www.saucedemo.com/")

    # Espera explícita para asegurar que el campo de usuario cargó
    wait = WebDriverWait(driver, 10)

    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()