import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def registrar_cliente_basico(driver):
    with allure.step("Ingresar al módulo Clientes"):
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '(//android.widget.LinearLayout[@resource-id="pe.restaurant.apprestaurant:id/constrain_component"])[2]'))
        ).click()

    with allure.step("Clic en 'Agregar cliente'"):
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((AppiumBy.ID, "pe.restaurant.apprestaurant:id/btn_agregar_cliente"))
        ).click()

    with allure.step("Completar datos básicos del cliente"):
        driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/edt_nombre_cliente").send_keys("Carlos")
        driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/edt_apellido_cliente").send_keys("Ruiz")
        driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/edt_limite_credito").send_keys("1000")
        driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/edt_direccion").send_keys("Av. Principal 123")
        driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/edt_telefono_cliente").send_keys("987654321")
        driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/edt_email_cliente").send_keys("carlos@mail.com")

    with allure.step("Guardar cliente básico"):
        driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/btn_guardar_cliente").click()
