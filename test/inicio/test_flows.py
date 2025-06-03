import allure
import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException, NoSuchElementException

def completar_flows(driver):
    with allure.step("Esperar la pantalla de carga hasta 100%"):
        try:
            elemento = WebDriverWait(driver, 30).until(
                EC.visibility_of_element_located((AppiumBy.ID, "pe.restaurant.apprestaurant:id/progress_status_message"))
            )
            try:
                progress_message = elemento.text
            except StaleElementReferenceException as e:
                allure.attach(f"Warning: {str(e)}", name="Warning StaleElementReference", attachment_type=allure.attachment_type.TEXT)
                # Re-obtener y leer de nuevo
                elemento = driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/progress_status_message")
                progress_message = elemento.text
            allure.attach(progress_message, name="Pantalla de Carga", attachment_type=allure.attachment_type.TEXT)
            screenshot = driver.get_screenshot_as_png()
            allure.attach(screenshot, name="Captura pantalla carga", attachment_type=allure.attachment_type.PNG)

        except TimeoutException as e:
            allure.attach(f"❌ Timeout esperando pantalla de carga: {str(e)}", name="Error Timeout", attachment_type=allure.attachment_type.TEXT)
            # Opcionalmente puedes decidir si quieres que falle la prueba o continuar
            # raise e

    # Continúa el resto del flujo con manejo de excepciones similares...
    with allure.step("Aperturar caja en cero si está disponible"):
        try:
            caja_abrir = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ID, "pe.restaurant.apprestaurant:id/tv_abrir_con_cero"))
            )
            if caja_abrir.is_displayed():
                caja_abrir.click()
                allure.attach("Se hizo clic en 'Aperturar caja en cero'", name="Acción caja", attachment_type=allure.attachment_type.TEXT)

                WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((AppiumBy.ID, "pe.restaurant.apprestaurant:id/tv_confirm"))
                ).click()
                allure.attach("Confirmación inicial presionada", name="Confirmación inicial", attachment_type=allure.attachment_type.TEXT)

                for digit in ["1", "2", "3", "4"]:
                    boton_pin = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{digit}")'))
                    )
                    boton_pin.click()
                    allure.attach(f"Dígito '{digit}' presionado", name="Ingreso PIN", attachment_type=allure.attachment_type.TEXT)

                boton_confirmar_pin = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((AppiumBy.ID, "pe.restaurant.apprestaurant:id/button_confirm"))
                )
                boton_confirmar_pin.click()
                allure.attach("PIN confirmado", name="Confirmación PIN", attachment_type=allure.attachment_type.TEXT)

                time.sleep(7)  # esperar animación

                boton_confirmar_final = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((AppiumBy.ID, "pe.restaurant.apprestaurant:id/confirm_button"))
                )
                boton_confirmar_final.click()
                allure.attach("Caja aperturada correctamente", name="Confirmación final", attachment_type=allure.attachment_type.TEXT)

                screenshot_final = driver.get_screenshot_as_png()
                allure.attach(screenshot_final, name="Caja Aperturada", attachment_type=allure.attachment_type.PNG)
            else:
                allure.attach("La opción de aperturar caja en cero no está disponible.", name="Info Caja", attachment_type=allure.attachment_type.TEXT)

        except (TimeoutException, NoSuchElementException) as e:
            allure.attach(f"❌ Error durante la apertura de caja: {str(e)}", name="Error Caja", attachment_type=allure.attachment_type.TEXT)
            raise Exception(f"Error al aperturar caja: {str(e)}")
