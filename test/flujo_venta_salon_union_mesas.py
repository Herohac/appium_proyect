import time
import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def venta_por_salon_union_mesas(driver):
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
            EC.element_to_be_clickable((AppiumBy.XPATH, '(//android.widget.LinearLayout[@resource-id="pe.restaurant.apprestaurant:id/relative_mesa"])[4]'))
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
          driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/button_number3").click()
          
          driver.find_element(AppiumBy.ID,"pe.restaurant.apprestaurant:id/iv_opciones_mesa").click()
          driver.find_element(AppiumBy.ID,"pe.restaurant.apprestaurant:id/ly_unir_mesas").click()
          
          WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '(//android.view.View[@resource-id="pe.restaurant.apprestaurant:id/iv_check"])[3]'))
          ).click()
          
          driver.find_element(AppiumBy.ID,"pe.restaurant.apprestaurant:id/btn_guardar_movimientos").click()
          
          WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '(//android.widget.LinearLayout[@resource-id="pe.restaurant.apprestaurant:id/relative_mesa"])[14]'))
          ).click()
          
          driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("1")').click()
          driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("2")').click()
          driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("3")').click()
          driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("4")').click()
              # Confirmar PIN
          driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/button_confirm").click()
          time.sleep(3)
          driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/button_number8").click()
          
          
          WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="pe.restaurant.apprestaurant:id/text_name_categoria" and @text="Bebidas"]'))
          ).click()
          
          driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/text_name_categoria").click()
          
          WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="pe.restaurant.apprestaurant:id/item"]/android.widget.LinearLayout'))
          ).click()
          
          WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="pe.restaurant.apprestaurant:id/text_name_productogeneral" and @text="Pepsi: 1 1/2 litro"]'))
          ).click()
          
          WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="pe.restaurant.apprestaurant:id/text_name_productogeneral" and @text="Pepsi: 1/2 litro"]'))
          ).click()
          
          WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="pe.restaurant.apprestaurant:id/text_name_productogeneral" and @text="Pepsi: 1 litro"]'))
           ).click() 
          
          WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.TextView[@text="Todas"]'))
           ).click()   
          
          WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="pe.restaurant.apprestaurant:id/text_name_categoria" and @text="Criollos"]'))
           ).click()  
           
          WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="pe.restaurant.apprestaurant:id/text_name_categoria" and @text="Carnes"]'))
           ).click()  
          
          WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="pe.restaurant.apprestaurant:id/text_name_productogeneral" and @text="Lomo a lo Pobre"]'))
           ).click()  
          
          WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="pe.restaurant.apprestaurant:id/text_name_productogeneral" and @text="Lomo Fino"]'))
           ).click()  
          
          WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="pe.restaurant.apprestaurant:id/text_name_productogeneral" and @text="TEST"]'))
           ).click() 
          
          driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/btn_ver_pedidos").click()
          driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/btn_agrupar").click()
          time.sleep(5)
          driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/btn_continuar").click()
          driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/btn_agregar_tarjeta").click()
          
          driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/ll_agregarpago").click()
          time.sleep(5)
          driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/cancel_button").click()
          driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/btn_nueva_venta").click()
          driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/navigation_principal").click()
          time.sleep(3)