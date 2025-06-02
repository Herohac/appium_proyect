import time
import allure
from test.appium_driver import start_appium_driver
from test.inicio.login_page import login
from test.inicio.local_page import seleccionar_local
from test.inicio.caja_page import seleccionar_caja
from test.inicio.test_flows import completar_flows
from test.turno_page import seleccionar_turno

def main():
    driver = start_appium_driver()
    usuario = "admin2@rest.pe"
    contrasena = "123456"
    with allure.step("Login"):
            login(driver, usuario, contrasena)
    with allure.step("Seleccionar local"):
            seleccionar_local(driver)
    with allure.step("Seleccionar Caja 03"):
            seleccionar_caja(driver)
    with allure.step("Seleccionar turno"):
            seleccionar_turno(driver)
    with allure.step("Presentar flujo de apertura de caja"):
            completar_flows(driver)
    time.sleep(2)
