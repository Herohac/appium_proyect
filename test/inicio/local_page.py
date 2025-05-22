from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def seleccionar_local(driver):
    local_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((AppiumBy.XPATH, '(//android.widget.RelativeLayout[@resource-id="pe.restaurant.apprestaurant:id/relative_mesa"])[1]/android.widget.FrameLayout'))
    )
    local_element.click()
