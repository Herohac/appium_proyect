import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def flujo_venta_rapida_sin_pagar(driver):
    with allure.step("ir a la seccion vender"): 
           venderclick = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.LinearLayout[@resource-id="pe.restaurant.apprestaurant:id/ll_vender"]'))
        )
           venderclick.click()
    with allure.step("Seleccionar venta rápida"):
        driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/btn_venta_rapida").click()
        driver.save_screenshot("venta_rapida.png")
        allure.attach.file("venta_rapida.png", name="Venta Rápida", attachment_type=allure.attachment_type.PNG)

    # Seleccionar Panadería
    with allure.step("Seleccionar categoría 'Panadería'"):
        driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="pe.restaurant.apprestaurant:id/text_name_categoria" and @text="Panaderia"]').click()

    # Seleccionar la subcategoría
    with allure.step("Seleccionar subcategoría"):
        driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="pe.restaurant.apprestaurant:id/text_name_productogeneral"]').click()

    # Seleccionar el tipo
    with allure.step("Seleccionar tipo de producto"):
        driver.find_element(AppiumBy.XPATH, '(//android.widget.FrameLayout[@resource-id="pe.restaurant.apprestaurant:id/item_variantes"])[1]/android.widget.LinearLayout/android.widget.LinearLayout').click()

    # Agregar la cantidad (4 unidades)
    with allure.step("Agregar 4 unidades"):
        driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/button_number4").click()
        driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/button_number0").click()
        driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/button_number0").click()
        driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/button_number0").click()

    # Confirmar la cantidad
    with allure.step("Confirmar cantidad"):
        driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/confirm_button").click()

    # Ver pedidos
    with allure.step("Ver pedidos"):
        driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/btn_ver_pedidos").click()

    # Enviar pedido
    with allure.step("Enviar pedido"):
        driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/btn_agrupar").click()
     
      #ir al pedido  sin  cobrar 
