# Pre-Entrega Automation Testing

Este proyecto automatiza flujos básicos de navegación, interacción y validación en el sitio web de pruebas **Sauce Demo** (www.saucedemo.com).

## Propósito del Proyecto

Demostrar la capacidad de aplicar estrategias de localización de elementos, esperas explícitas y validación de estados del DOM mediante pruebas automatizadas independientes y estructuradas.

## Tecnologías Utilizadas

- **Python:** Lenguaje principal de programación.
- **Selenium WebDriver:** Herramienta para la automatización y control del navegador.
- **Pytest:** Framework para la estructuración y ejecución de pruebas.
- **pytest-html:** Plugin para la generación de reportes visuales en formato HTML.

## Estructura del Proyecto

- `tests/`: Contiene los casos de prueba principales.
- `utils/`: Contiene funciones auxiliares para evitar repetición de código (`helpers.py`).
- `reports/`: Directorio donde se generan los reportes HTML y las capturas de pantalla automáticas en caso de que un test falle.
- `conftest.py`: Archivo de configuración de Pytest (manejo del driver y capturas).

## Instrucciones de Instalación

1. Clonar el repositorio.
2. Crear un entorno virtual e instalar las dependencias:
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # En Windows
   pip install -r requirements.txt
   ```

## Ejecución de Pruebas
Para ejecutar toda la suite de pruebas y generar el reporte HTML autocontenido:
```bash
pytest
```
Para ejecutar un módulo específico (por ejemplo, solo login):
```bash
pytest tests/test_login.py
```