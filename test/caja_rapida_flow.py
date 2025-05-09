import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def flujo_caja_rapida(driver):
    # Seleccionar el botón de Venta Rápida
    with allure.step("ir a la seccion vender"): 
           venderclick = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.LinearLayout[@resource-id="pe.restaurant.apprestaurant:id/ll_vender"]'))
        )
           venderclick.click()
          
    with allure.step("Seleccionar el botón de venta rápida"):
        driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/btn_venta_rapida").click()
        driver.save_screenshot("venta_rapida.png")
        allure.attach.file("venta_rapida.png", name="Venta Rápida", attachment_type=allure.attachment_type.PNG)

    # Seleccionar la categoría "Bebidas"
    with allure.step("Seleccionar categoría 'Bebidas'"):
         driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Bebidas")').click()

    # Seleccionar la subcategoría
         driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/text_name_categoria").click()

    # Seleccionar un producto
         driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/text_name_productogeneral").click()

    # Seleccionar presentación del producto
         driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Pepsi: 1 litro")').click()

    # Seleccionar otra presentación
         driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Pepsi: 1 1/2 litro")').click()

    # Ver pedidos
         driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/btn_ver_pedidos").click()

    # Agrupar pedidos
         driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/btn_agrupar").click()

    