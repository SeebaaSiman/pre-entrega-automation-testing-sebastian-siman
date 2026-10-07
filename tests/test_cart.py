from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import login_standard_user

def test_agregar_producto_al_carrito(driver):
    """Caso Positivo: Agregar producto, verificar badge y presencia en carrito."""
    login_standard_user(driver)
    wait = WebDriverWait(driver, 10)

# Añadir el primer producto al carrito
    boton_add_to_cart = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[text()='Add to cart'])[1]")))
    boton_add_to_cart.click()

  # Verificar que el contador del carrito se incremente a 1
    carrito_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert carrito_badge.text == "1", "El contador del carrito no se incrementó correctamente"


   # Navegar al carrito de compras
    icono_carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    icono_carrito.click()


   # Comprobar que el producto añadido aparezca en el carrito
    wait.until(EC.url_contains("/cart.html"))

    items_en_carrito = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(items_en_carrito) == 1, "El producto no se visualiza en el carrito"

def test_remover_producto_del_carrito(driver):
    """Caso Positivo: Eliminar un producto agregado y verificar que el badge desaparezca."""
    login_standard_user(driver)
    wait = WebDriverWait(driver, 10)

    # Agregar producto
    boton_add_to_cart = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[text()='Add to cart'])[1]")))
    boton_add_to_cart.click()

    # Remover el mismo producto
    boton_remove = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Remove']")))
    boton_remove.click()

    # Verificar que el badge del carrito ya no exista en el DOM
    carrito_badge = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
    assert len(carrito_badge) == 0, "El badge del carrito no desapareció al remover el producto"

def test_carrito_fallo_intencional(driver):
    """Fallo Intencional: Fuerza un error esperando 99 productos en el badge del carrito."""
    # login
    login_standard_user(driver)
    # espera explícita
    wait = WebDriverWait(driver, 10)

    # Agregar producto
    boton_add_to_cart = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[text()='Add to cart'])[1]")))
    boton_add_to_cart.click()

    # Aserción errónea intencional
    carrito_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert carrito_badge.text == "99", "Fallo intencional: El número de items en el badge no es 99"