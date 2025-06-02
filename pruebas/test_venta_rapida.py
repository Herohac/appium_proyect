import allure
from test.appium_driver import start_appium_driver
from test.venta_rapida.caja_rapida_flow import flujo_caja_rapida

def main(driver):
    with allure.step("Ejecutar flujo de caja rápida"):
        flujo_caja_rapida(driver)
    # Otros flujos de venta rápida si quieres
