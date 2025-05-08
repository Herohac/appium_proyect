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
    with allure.step("Seleccionar subcategoría"):
        driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/text_name_categoria").click()

    # Seleccionar un producto
    with allure.step("Seleccionar producto"):
        driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/text_name_productogeneral").click()

    # Seleccionar presentación del producto
    with allure.step("Seleccionar presentación 'Pepsi: 1 litro'"):
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Pepsi: 1 litro")').click()

    # Seleccionar otra presentación
    with allure.step("Seleccionar presentación 'Pepsi: 1 1/2 litro'"):
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Pepsi: 1 1/2 litro")').click()

    # Ver pedidos
    with allure.step("Ver pedidos"):
        driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/btn_ver_pedidos").click()

    # Agrupar pedidos
    with allure.step("Agrupar pedidos"):
        driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/btn_agrupar").click()

    # Seleccionar el método de pago: Efectivo
    with allure.step("Seleccionar método de pago: Efectivo"):
        driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/btn_agregar_efectivo").click()

    # Seleccionar tipo de pago: Exacto
    with allure.step("Seleccionar tipo de pago: Exacto"):
        driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/btn_exacto").click()

    # Esperar unos segundos para que se complete la venta
    with allure.step("Esperar a que la venta se complete (espera de 3 segundos)"):
        time.sleep(3)

    # Verificar si la impresora imprimió
    with allure.step("Verificar si se imprimió el recibo"):
        try:
            # Aquí puedes verificar si se imprimió correctamente
            # Si no, hacer clic en cancelar
            driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/cancel_button").click()
            allure.attach("Venta no impresa. Se canceló.", name="Advertencia de impresión", attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            allure.attach(f"Error al verificar impresión: {str(e)}", name="Error Impresión", attachment_type=allure.attachment_type.TEXT)

    # Hacer clic en nueva venta
    with allure.step("Iniciar nueva venta"):
        driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/btn_nueva_venta").click()

    # Salir de la venta rápida y volver a la pantalla general
    with allure.step("Salir de la venta rápida"):
        driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/ly_back").click()

    driver.save_screenshot("flujo_caja_rapida_completo.png")
    allure.attach.file("flujo_caja_rapida_completo.png", name="Flujo de Caja Rápida Completado", attachment_type=allure.attachment_type.PNG)
