import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def registrar_cliente_avanzado(driver):
    with allure.step("Ingresar al módulo Clientes"):
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '(//android.widget.LinearLayout[@resource-id="pe.restaurant.apprestaurant:id/constrain_component"])[2]'))
        ).click()

    with allure.step("Clic en 'Agregar cliente'"):
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((AppiumBy.ID, "pe.restaurant.apprestaurant:id/btn_agregar_cliente"))
        ).click()

    with allure.step("Activar registro avanzado"):
        driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/cly_registroavanzado").click()

    with allure.step("Completar datos avanzados del cliente"):
        driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/edt_ruc_cliente").send_keys("70891234")
        driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/edt_nombre_cliente").send_keys("Pedro")
        driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/edt_apellido_cliente").send_keys("Gómez")
        driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/edt_limite_credito").send_keys("2000")
        driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/edt_direccion").send_keys("Calle Central 456")
        driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/edt_telefono_cliente").send_keys("912345678")
        driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/edt_email_cliente").send_keys("pedro@mail.com")

    with allure.step("Guardar cliente avanzado"):
        driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/btn_guardar_cliente").click()
