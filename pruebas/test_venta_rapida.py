import unittest
import allure
from test.appium_driver import start_appium_driver
from test.inicio.login_page import login
from test.inicio.local_page import seleccionar_local
from test.inicio.caja_page import seleccionar_caja
from test.inicio.test_flows import completar_flows
from test.turno_page import seleccionar_turno
from test.venta_rapida.caja_rapida_flow import flujo_caja_rapida
from test.venta_rapida.venta_rapida_modificadores import flujo_venta_rapida_con_modificadores
from test.venta_rapida.venta_rapida_cantidades import flujo_venta_rapida_con_cantidades
from test.venta_rapida.venta_rapida_favoritos import flujo_venta_rapida_desde_favoritos
from test.venta_salon.flujo_venta_salon import venta_por_salon
from test.venta_salon.flujo_venta_salon_con_cliente import venta_por_salon_con_cliente
from test.venta_salon.flujo_venta_salon_union_mesas import venta_por_salon_union_mesas
from test.venta_salon.flujo_venta_salon_mover_pedidos import venta_por_salon_mover_pedidos
from test.venta_rapida.venta_rapida_sin_pagar import flujo_venta_rapida_sin_pagar
from test.venta_rapida.venta_rapida_busqueda import venta_rapida_busqueda
from test.venta_salon.flujo_venta_salon_busqueda import venta_por_salon_busqueda
from test.flujo_cobro_pedido import cobrar_pedido
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@allure.epic("venta rapida de prueba")
class Testventarapida(unittest.TestCase):

    def main():
     driver = start_appium_driver()  # Sin self
     with allure.step("Ejecutar flujo de caja rápida"):
        flujo_caja_rapida(driver)
    if __name__ == '__main__':
       main()