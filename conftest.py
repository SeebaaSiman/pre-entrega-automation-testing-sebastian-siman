import pytest
from selenium import webdriver
from datetime import datetime
import os

FECHA_ACTUAL = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
REPORTS_DIR = os.path.join("reports", FECHA_ACTUAL)

def pytest_configure(config):
    """Crea la subcarpeta con la fecha y define dinámicamente la ruta del reporte HTML."""
    if not os.path.exists(REPORTS_DIR):
        os.makedirs(REPORTS_DIR)

    # Sobrescribe la opción de salida HTML para dirigirla a la carpeta con fecha
    config.option.htmlpath = os.path.join(REPORTS_DIR, "reporte.html")


@pytest.fixture(scope="function")
def driver():
    # Configuración del navegador Chrome
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    # Inicializar el WebDriver
    driver = webdriver.Chrome(options=options)

    yield driver

    # Teardown: se ejecuta después de cada test
    driver.quit()

# Hook para tomar capturas de pantalla en caso de fallo
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    # Capturar pantalla si el test falla durante la fase de ejecución
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            file_name = f"screenshot_error_{item.name}.png"
            file_path = os.path.join(REPORTS_DIR, file_name)
            driver.save_screenshot(file_path)