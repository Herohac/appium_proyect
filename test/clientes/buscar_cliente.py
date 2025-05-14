import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def buscar_cliente(driver):
    with allure.step("Ingresar al módulo Clientes"):
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '(//android.widget.LinearLayout[@resource-id="pe.restaurant.apprestaurant:id/constrain_component"])[2]'))
        ).click()

    with allure.step("Click en el buscador"):
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "pe.restaurant.apprestaurant:id/search_src_text"))
        ).click()

    with allure.step("Escribir apellido del cliente a buscar"):
        campo_busqueda = driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/search_src_text")
        campo_busqueda.send_keys("Gómez")
