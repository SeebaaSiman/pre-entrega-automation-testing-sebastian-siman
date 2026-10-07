import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Lista de usuarios a probar en el test parametrizado
USUARIOS_LOGIN = [
    "standard_user",
    "problem_user",
    "performance_glitch_user",
    "error_user",
    "visual_user",
    # xfail indica a pytest que esperamos que este caso falle porque el usuario está bloqueado
    pytest.param("locked_out_user", marks=pytest.mark.xfail(reason="Usuario bloqueado por el sistema"))
]
@pytest.mark.parametrize("username", USUARIOS_LOGIN) # Esto genera un caso de prueba independiente para cada usuario de la lista.

def test_login_exitoso(driver, username):
    """Caso Positivo: Verifica el inicio de sesión con distintos roles de usuario."""
    driver.get("https://www.saucedemo.com/")
    # Espera explícita para asegurar que el campo de usuario cargó
    wait = WebDriverWait(driver, 10)

# Ingreso de credenciales
    user_input = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    user_input.send_keys(username)
    password_input.send_keys("secret_sauce")
    login_button.click()

    # Validaciones de login exitoso
    ## Validar que la URL contiene /inventory.html

    wait.until(EC.url_contains("/inventory.html"))
    assert "inventory.html" in driver.current_url

    ## Validar que aparezca el título de la página (Swag Labs / Products)

    logo = driver.find_element(By.CLASS_NAME, "app_logo")
    assert logo.text == "Swag Labs"

    title = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))
    assert title.text.lower() == "products"


def test_login_usuario_bloqueado(driver):
    """Caso Negativo: Intento de login con un usuario bloqueado."""
    driver.get("https://www.saucedemo.com/")
    wait = WebDriverWait(driver, 10)

    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("locked_out_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    error_message = wait.until(EC.visibility_of_element_located((By.XPATH, "//h3[@data-test='error']")))
    assert "Sorry, this user has been locked out." in error_message.text

def test_login_credenciales_invalidas(driver):
    """Caso Negativo: Intento de login con contraseña incorrecta."""
    driver.get("https://www.saucedemo.com/")
    wait = WebDriverWait(driver, 10)

    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("clave_incorrecta")
    driver.find_element(By.ID, "login-button").click()

    error_message = wait.until(EC.visibility_of_element_located((By.XPATH, "//h3[@data-test='error']")))
    assert "Username and password do not match" in error_message.text

def test_login_fallo_intencional(driver):
    """Fallo Intencional: Fuerza un error de aserción al esperar una URL incorrecta."""
    driver.get("https://www.saucedemo.com/")
    wait = WebDriverWait(driver, 10)

    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    wait.until(EC.url_contains("/inventory.html"))
    
    # Aserción errónea intencional para generar la captura de pantalla
    assert "dashboard.html" in driver.current_url, "Fallo intencional: Se esperaba estar en dashboard.html"