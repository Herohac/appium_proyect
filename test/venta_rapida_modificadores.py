import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def flujo_venta_rapida_con_modificadores(driver):
    # Hacer clic en 'Vender'
    with allure.step("ir a la seccion vender"): 
           venderclick = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.LinearLayout[@resource-id="pe.restaurant.apprestaurant:id/ll_vender"]'))
        )
           venderclick.click()
    # Hacer clic en 'Venta rápida'
    with allure.step("Seleccionar venta rápida"):
        driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/btn_venta_rapida").click()
        driver.save_screenshot("venta_rapida.png")
        allure.attach.file("venta_rapida.png", name="Venta Rápida", attachment_type=allure.attachment_type.PNG)

    # Seleccionar la categoría "Hamburguesas"
    with allure.step("Seleccionar categoría 'Hamburguesas'"):
        driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="pe.restaurant.apprestaurant:id/text_name_categoria" and @text="Hamburguesas"]').click()

    # Seleccionar la subcategoría "Clásica"
    with allure.step("Seleccionar subcategoría 'Clásica'"):
        driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="pe.restaurant.apprestaurant:id/text_name_productogeneral" and @text="Clásica"]').click()

    # Seleccionar la presentación "Clásica: pequeña"
    with allure.step("Seleccionar presentación 'Clásica: pequeña'"):
        driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="pe.restaurant.apprestaurant:id/text_name_productogeneral" and @text="Clásica: pequeña"]').click()

    # Agregar 2 modificadores
    with allure.step("Agregar 2 modificadores"):
        driver.find_element(AppiumBy.XPATH, '(//android.widget.CheckBox[@resource-id="pe.restaurant.apprestaurant:id/cb_modificadorseleccion"])[3]').click()
        driver.find_element(AppiumBy.XPATH, '(//android.widget.CheckBox[@resource-id="pe.restaurant.apprestaurant:id/cb_modificadorseleccion"])[4]').click()

    # Agregar una nota
    with allure.step("Agregar una nota 'LA CARNE A TERMINO MEDIO'"):
        driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/et_nota").send_keys("LA CARNE A TERMINO MEDIO")

    # Guardar los modificadores
    with allure.step("Guardar los modificadores"):
        driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/btn_modificadores_guardar").click()

    # Regresar con el botón de atrás del celular (usando keycode)
    with allure.step("Regresar con el botón de atrás del celular"):
        driver.press_keycode(4)

    # Ver pedidos
    with allure.step("Ver pedidos"):
        driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/btn_ver_pedidos").click()

    # Enviar pedidos
    with allure.step("Enviar pedidos"):
        driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/btn_agrupar").click()

    # Seleccionar método de pago "Efectivo"
    with allure.step("Seleccionar método de pago: Efectivo"):
        driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/btn_agregar_efectivo").click()

    # Seleccionar "Agregar Pago"
    with allure.step("Seleccionar 'Agregar Pago'"):
        driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/ll_agregarpago").click()

    # Esperar 3 segundos para verificación
    with allure.step("Esperar 3 segundos para verificar si se imprimió o no"):
        time.sleep(3)

    # Verificar si la impresora imprimió
    with allure.step("Verificar si se imprimió el recibo"):
        try:
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

    driver.save_screenshot("flujo_venta_rapida_completo.png")
    allure.attach.file("flujo_venta_rapida_completo.png", name="Flujo de Venta Rápida Completado", attachment_type=allure.attachment_type.PNG)
