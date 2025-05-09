import unittest
import allure
from test.appium_driver import start_appium_driver
from test.login_page import login
from test.local_page import seleccionar_local
from test.caja_page import seleccionar_caja
from test.test_flows import completar_flows
from test.turno_page import seleccionar_turno
from test.caja_rapida_flow import flujo_caja_rapida
from test.venta_rapida_modificadores import flujo_venta_rapida_con_modificadores
from test.venta_rapida_cantidades import flujo_venta_rapida_con_cantidades
from test.venta_rapida_favoritos import flujo_venta_rapida_desde_favoritos
from test.flujo_venta_salon import venta_por_salon
from test.flujo_venta_salon_con_cliente import venta_por_salon_con_cliente
from test.flujo_venta_salon_union_mesas import venta_por_salon_union_mesas
from test.flujo_venta_salon_mover_pedidos import venta_por_salon_mover_pedidos
from test.venta_rapida_sin_pagar import flujo_venta_rapida_sin_pagar
from test.venta_rapida_busqueda import venta_rapida_busqueda
from test.flujo_cobro_pedido import cobrar_pedido
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@allure.epic("Inicio de app y navegación")
class TestInicioSesion(unittest.TestCase):

    def setUp(self):
        self.driver = start_appium_driver()

    @allure.title("Login completo con selección de local, caja y turno")
    def test_login_completo_y_seleccion(self):
        usuario = "admin2@rest.pe"
        contrasena = "123456"

        with allure.step("Login"):
            login(self.driver, usuario, contrasena)

        with allure.step("Seleccionar local"):
            seleccionar_local(self.driver)

        with allure.step("Seleccionar Caja 03"):
            seleccionar_caja(self.driver)

        with allure.step("Seleccionar turno"):
            seleccionar_turno(self.driver)
            
        with allure.step("Presentar flujo de apertura de caja"):
            completar_flows(self.driver)

        # Esperar 5 segundos para asegurar que la animación se complete
        time.sleep(2)  # Puedes cambiar esto por un WebDriverWait si prefieres más control


          # venta  simple rápida: 
        #with allure.step("Ejecutar flujo de caja rápida"):
        #     flujo_caja_rapida(self.driver)
        
        #venta rápida con busqueda y modificadores
        with allure.step("venta rápida con busqueda y modificadores"):
             venta_rapida_busqueda(self.driver)
             
           #venta  simple por  salón: 
       # with allure.step("Ejecutar flujo de venta por salon"):
       #      venta_por_salon(self.driver)
       
           
       
       
       
       
       
       
       # with allure.step("Ejecutar flujo de caja rápida"):
       #     flujo_venta_rapida_con_modificadores(self.driver)
       
        #with allure.step("Ejecutar flujo de caja rápida con  cantidades"):
         #    flujo_venta_rapida_con_cantidades(self.driver)
            
       # with allure.step("Ejecutar flujo de caja rápida favoritos"):
        #     flujo_venta_rapida_desde_favoritos(self.driver)
    
      #  with allure.step("Ejecutar flujo de venta por salon"):
      #       venta_por_salon(self.driver)
        
       # with allure.step("ejecutar  cliente en venta por salon"): 
        #     venta_por_salon_con_cliente(self.driver)
        
        #with allure.step("venta por salón con  unión  de mesas"):      
         #    venta_por_salon_union_mesas(self.driver)
       
        #with allure.step("venta por salón con  unión  de mesas"):      
        #      venta_por_salon_mover_pedidos(self.driver)
     
     
     
        with allure.step("cobro"):          
           #  flujo_venta_rapida_sin_pagar(self.driver)
            cobrar_pedido(driver=self.driver, comprobante="nota", metodo_pago="plin", tarjeta_tipo="") 
        
    def tearDown(self):
        self.driver.quit()
        
        