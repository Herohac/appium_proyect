from appium.webdriver.common.appiumby import AppiumBy

def login(driver, usuario, contrasena):
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Iniciar sesión")').click()
    driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/edt_login_usuario").send_keys(usuario)
    driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/edt_password_usuario").send_keys(contrasena)
    driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/btn_iniciar_sesion").click()
