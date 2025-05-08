import time
import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def cobrar_pedido(driver, comprobante="Boleta", metodo_pago="Efectivo", tarjeta_tipo=None):
    with allure.step(f"Seleccionar comprobante: {comprobante}"):
        if comprobante.lower() == "factura":
            driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="Factura"]').click()
            driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/tv_agregar_cliente").click()
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.TextView[@text="Adrianzen cordova andre kaled"]'))
            ).click()
        elif comprobante.lower() == "nota":
            driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="Nota de Venta"]').click()
        else:
            driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="Boleta"]').click()

    with allure.step(f"Seleccionar método de pago: {metodo_pago}"):
        if metodo_pago.lower() == "efectivo":
            driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/btn_agregar_efectivo").click()
            driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/btn_exacto").click()
        elif metodo_pago.lower() == "tarjeta":
            driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/btn_agregar_tarjeta").click()
            if tarjeta_tipo:
                driver.find_element(AppiumBy.XPATH, f'//android.widget.TextView[@text="{tarjeta_tipo}"]').click()
        elif metodo_pago.lower() == "otros":
            driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/btn_agregar_metodo_pago").click()
            time.sleep(1)
            driver.find_elemento(AppiumBy.ID, "pe.restaurant.apprestaurant:id/ll_agregarpago").click()
            time.sleep(2)
            try:
                confirm = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((AppiumBy.ID, "pe.restaurant.apprestaurant:id/confirm_button"))
                )
                confirm.click()
                driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/btn_eliminar_metodo_pago").click()
                driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/btn_agregar_metodo_pago").click()
                driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/btn_descuento").click()
                time.sleep(1)
                driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/ll_agregarpago").click()
            except:
                pass
        elif metodo_pago.lower() == "plin":
            driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/iv_opcion_plin").click()
        elif metodo_pago.lower() == "yape":
            for _ in range(3):
                driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/iv_metodo_pago_arrow_right").click()
            driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/iv_opcion_yape").click()
        elif metodo_pago.lower() == "izipay":
            for _ in range(3):
                driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/iv_metodo_pago_arrow_right").click()
            driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/iv_opcion_izipay").click()

    with allure.step("Agregar pago"):
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
