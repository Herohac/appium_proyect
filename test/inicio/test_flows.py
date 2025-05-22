import allure
import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def completar_flows(driver):
    # Espera a que aparezca la pantalla de carga
    with allure.step("Esperar la pantalla de carga hasta 100%"):
        WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((AppiumBy.ID, "pe.restaurant.apprestaurant:id/progress_status_message"))
        )
        # Puedes agregar un paso adicional para verificar el progreso (de 0 a 100%)
        progress_message = driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/progress_status_message").text
        allure.attach(progress_message, name="Pantalla de Carga", attachment_type=allure.attachment_type.TEXT)
    
    with allure.step("Aperturar caja en cero si está disponible"):
        try:
            caja_abrir = driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/tv_abrir_con_cero")
            if caja_abrir.is_displayed():
                caja_abrir.click()

                # Confirmación inicial
                WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((AppiumBy.ID, "pe.restaurant.apprestaurant:id/tv_confirm"))
                ).click()

                # Ingresar PIN: 4 3 2 1
                driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("1")').click()
                driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("2")').click()
                driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("3")').click()
                driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("4")').click()

                # Confirmar PIN
                driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/button_confirm").click()
                allure.attach("PIN ingresado y confirmado", name="Ingreso PIN", attachment_type=allure.attachment_type.TEXT)

                # Esperar la animación de apertura (7 segundos)
                time.sleep(7)

                # Confirmación final
                WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((AppiumBy.ID, "pe.restaurant.apprestaurant:id/confirm_button"))
                ).click()
                allure.attach("Caja aperturada correctamente", name="Confirmación final", attachment_type=allure.attachment_type.TEXT)

        except Exception as e:
            allure.attach(f"❌ Error durante la apertura de caja: {str(e)}", name="Error Caja", attachment_type=allure.attachment_type.TEXT)
            raise Exception(f"Error al aperturar caja: {str(e)}")

    # Fin del flujo
    driver.save_screenshot("flujo_caja_aperturada.png")
    allure.attach.file("flujo_caja_aperturada.png", name="Caja Aperturada", attachment_type=allure.attachment_type.PNG)
