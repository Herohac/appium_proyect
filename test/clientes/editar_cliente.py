import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def editar_cliente(driver):
    with allure.step("Seleccionar cliente de la lista para editar"):
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '(//android.widget.LinearLayout[@resource-id="pe.restaurant.apprestaurant:id/ly_editar_cliente"])[1]/android.widget.LinearLayout/android.widget.LinearLayout'))
        ).click()

    with allure.step("Editar nombre del cliente a 'MARIO'"):
        campo_nombre = driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/edt_nombre_cliente")
        campo_nombre.clear()
        campo_nombre.send_keys("MARIO")

    with allure.step("Guardar cambios"):
        driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/btn_guardar_cliente").click()
