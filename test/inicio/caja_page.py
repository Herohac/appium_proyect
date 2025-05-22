import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def seleccionar_caja(driver):
    try:
        # Utilizar el XPath que selecciona específicamente la Caja 03
        caja_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="pe.restaurant.apprestaurant:id/img_icon_sucursal"])[3]')
            )
        )
        caja_element.click()
        driver.save_screenshot("caja_seleccionada.png")
        allure.attach.file("caja_seleccionada.png", name="Caja 03 Seleccionada", attachment_type=allure.attachment_type.PNG)
    except Exception as e:
        allure.attach(f"❌ Error al seleccionar la caja: {str(e)}", name="Error Caja", attachment_type=allure.attachment_type.TEXT)
        raise Exception(f"No se encontró la Caja 03")
