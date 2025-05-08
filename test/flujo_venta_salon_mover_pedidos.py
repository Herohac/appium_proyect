import time
import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def venta_por_salon_mover_pedidos(driver):
    with allure.step("Clic en 'Vender'"):
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((AppiumBy.ID, "pe.restaurant.apprestaurant:id/ll_vender"))
        ).click()

    with allure.step("Clic en 'Ver salones'"):
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((AppiumBy.ID, "pe.restaurant.apprestaurant:id/ll_ver_salones"))
        ).click()

    with allure.step("Seleccionar salón 'Diego'"):
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.Button[@resource-id="pe.restaurant.apprestaurant:id/btn_salon" and @text="Diego"]'))
        ).click()
        
    with allure.step("Seleccionar la primera mesa disponible"):
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '(//android.widget.LinearLayout[@resource-id="pe.restaurant.apprestaurant:id/relative_mesa"])[8]'))
        ).click()
        
    with allure.step("Ingresar PIN 4321"):
          driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("1")').click()
          driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("2")').click()
          driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("3")').click()
          driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("4")').click()
              # Confirmar PIN
          driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/button_confirm").click()
          allure.attach("PIN ingresado y confirmado", name="Ingreso PIN", attachment_type=allure.attachment_type.TEXT)
            # Esperar la animación de apertura (7 segundos)
          time.sleep(3)
         
          driver.find_element(AppiumBy.ID,"pe.restaurant.apprestaurant:id/iv_opciones_mesa").click()
          driver.find_element(AppiumBy.ID,"pe.restaurant.apprestaurant:id/ly_mover_pedidos").click()
          
          driver.find_element(AppiumBy.ID,"pe.restaurant.apprestaurant:id/cb_selecionar_todos").click()  
          driver.find_element(AppiumBy.ID,"pe.restaurant.apprestaurant:id/btn_guardar_movimientos").click()  
          
    with allure.step("Seleccionar la primera mesa disponible"):
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.GridView[@resource-id="pe.restaurant.apprestaurant:id/rv_salon"]/android.widget.LinearLayout[2]'))
        ).click()
        
    with allure.step("Seleccionar la primera mesa a mover  el  pedido"):
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="pe.restaurant.apprestaurant:id/tv_descripcion" and @text="M10"]'))
        ).click()     
           
        driver.find_element(AppiumBy.ID,"pe.restaurant.apprestaurant:id/btn_guardar").click()
        driver.find_element(AppiumBy.ID,"pe.restaurant.apprestaurant:id/confirm_button").click() 
        
    with allure.step("Seleccionar la primera mesa disponible"):
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="pe.restaurant.apprestaurant:id/txt_n_mesa" and @text="M10"]'))
        ).click()  
        
    with allure.step("Ingresar PIN 4321"):
          driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("1")').click()
          driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("2")').click()
          driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("3")').click()
          driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("4")').click()
              # Confirmar PIN
          driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/button_confirm").click()
          allure.attach("PIN ingresado y confirmado", name="Ingreso PIN", attachment_type=allure.attachment_type.TEXT)
          
          
          #ver pedidos 
          driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/btn_ver_pedidos").click()
          
          #cobrar el pedido
          driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/btn_continuar").click()
          
          #seleccionar tarjeta 
          driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/btn_agregar_tarjeta").click()
          
          #generar  el pago
          driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/ll_agregarpago").click()
         #esperar  el error de  la  immpresión
          time.sleep(5)
          #cqncelar  la  impresión
          driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/cancel_button").click()
          #generar  una nueva  venta
          driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/btn_nueva_venta").click()
          #ir a  la navegación  principal 
          driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/navigation_principal").click()
          time.sleep(3)