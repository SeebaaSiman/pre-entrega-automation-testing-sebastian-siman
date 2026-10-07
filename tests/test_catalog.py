from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import login_standard_user

def test_verificacion_catalogo(driver):
    """Caso Positivo: Validar títulos, productos, menú y filtros en el catálogo."""

    login_standard_user(driver)

    # Espera explícita para asegurar que el campo de usuario cargó
    wait = WebDriverWait(driver, 10)

 # Validar que el título de la pestaña (HTML title) sea correcto
    assert driver.title == "Swag Labs"

    # Comprobar que existan productos visibles
    wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item")))
    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(productos) > 0, "No se encontraron productos en la página"

 # Validar elementos importantes de la interfaz (menú y filtros)
    menu_hamburguesa = driver.find_element(By.ID, "react-burger-menu-btn")
    filtro_dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")
    assert menu_hamburguesa.is_displayed()
    assert filtro_dropdown.is_displayed()

# Listar nombre y precio del primer producto
    nombre_primer_prod = productos[0].find_element(By.CLASS_NAME, "inventory_item_name").text
    precio_primer_prod = productos[0].find_element(By.CLASS_NAME, "inventory_item_price").text
    print(f"\n[INFO] Primer producto: {nombre_primer_prod} - {precio_primer_prod}")

def test_acceso_no_autorizado_inventario(driver):
    """Caso Negativo: Intentar acceder directamente a /inventory.html sin estar logueado."""
    driver.get("https://www.saucedemo.com/inventory.html")
    wait = WebDriverWait(driver, 10)

    # Debe redirigir o mostrar un mensaje de error impidiendo el acceso
    error_message = wait.until(EC.visibility_of_element_located((By.XPATH, "//h3[@data-test='error']")))
    assert "You can only access '/inventory.html' when you are logged in." in error_message.text

def test_catalogo_fallo_intencional(driver):
    """Fallo Intencional: Fuerza un error al verificar un título del sitio incorrecto."""
    login_standard_user(driver)
    WebDriverWait(driver, 10).until(EC.url_contains("/inventory.html"))

    # Aserción errónea intencional
    assert driver.title == "Tienda Ficticia Incorrecta", "Fallo intencional: El título esperado no coincide"