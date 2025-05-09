import time
import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def venta_por_salon(driver):
    with allure.step("Clic en 'Vender'"):
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((AppiumBy.ID, "pe.restaurant.apprestaurant:id/ll_vender"))
        ).click()

    with allure.step("Clic en 'Ver salones'"):
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((AppiumBy.ID, "pe.restaurant.apprestaurant:id/ll_ver_salones"))
        ).click()

    with allure.step("Seleccionar salón 'Diego'"):
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.Button[@resource-id="pe.restaurant.apprestaurant:id/btn_salon" and @text="Diego"]'))
        ).click()

    with allure.step("Seleccionar la primera mesa disponible"):
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '(//android.widget.LinearLayout[@resource-id="pe.restaurant.apprestaurant:id/relative_mesa"])[1]'))
        ).click()

    with allure.step("Ingresar PIN 4321"):
          driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("1")').click()
          driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("2")').click()
          driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("3")').click()
          driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("4")').click()
              # Confirmar PIN
          driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/button_confirm").click()
          allure.attach("PIN ingresado y confirmado", name="Ingreso PIN", attachment_type=allure.attachment_type.TEXT)
            # Esperar la animación de apertura (7 segundos)
          time.sleep(3)

    with allure.step("Seleccionar 3 personas"):
        driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/button_number3").click()
    
    with allure.step("click en  busqueda"): 
        driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/tv_busqueda").click()
        

    with allure.step("Escribir 'combo' en el campo de búsqueda"):
         campo_busqueda = WebDriverWait(driver, 10).until(
         EC.presence_of_element_located((AppiumBy.ID, "pe.restaurant.apprestaurant:id/search_src_text"))
         )
         campo_busqueda.clear()
         campo_busqueda.set_value("combo")


    with allure.step("Agregar primer combo de la lista"):
        driver.find_element(AppiumBy.XPATH, '(//android.widget.Button[@resource-id="pe.restaurant.apprestaurant:id/bt_agregar"])[1]').click()

    with allure.step("Seleccionar Hawaiana pequeña y mediana"):
        driver.find_element(AppiumBy.XPATH, '(//android.widget.RadioButton[@resource-id="pe.restaurant.apprestaurant:id/rb_detallecombo"])[2]').click()
        driver.find_element(AppiumBy.XPATH, '(//android.widget.RadioButton[@resource-id="pe.restaurant.apprestaurant:id/rb_detallecombo"])[4]').click()

    with allure.step("Seleccionar adicional Pepsi 1/2 litro"):
        driver.find_element(AppiumBy.XPATH, '(//android.widget.CheckBox[@resource-id="pe.restaurant.apprestaurant:id/cb_adicionalcombo"])[1]').click()

    with allure.step("Aumentar cantidad del adicional seleccionado"):
        plus_button = driver.find_element(AppiumBy.XPATH, '(//android.widget.LinearLayout[@resource-id="pe.restaurant.apprestaurant:id/ly_plus"])[1]')
        plus_button.click()
        plus_button.click()

    with allure.step("Confirmar selección"):
        driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/confirm_button").click()

    with allure.step("Volver a la pantalla principal"):
        driver.find_element(AppiumBy.XPATH, '//android.widget.LinearLayout[@resource-id="pe.restaurant.apprestaurant:id/ly_back"]/android.widget.ImageView').click()

    with allure.step("Seleccionar categoría 'Criollos'"):
        driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="pe.restaurant.apprestaurant:id/text_name_categoria" and @text="Criollos"]').click()

    with allure.step("Seleccionar subcategoría"):
        driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/text_name_productogeneral").click()

    with allure.step("Seleccionar Lomo Saltado familiar, personal y mediano"):
        driver.find_element(AppiumBy.XPATH, '(//android.widget.RadioButton[@resource-id="pe.restaurant.apprestaurant:id/rb_detallecombo"])[2]').click()
        driver.find_element(AppiumBy.XPATH, '(//android.widget.RadioButton[@resource-id="pe.restaurant.apprestaurant:id/rb_detallecombo"])[4]').click()
        driver.find_element(AppiumBy.XPATH, '(//android.widget.RadioButton[@resource-id="pe.restaurant.apprestaurant:id/rb_detallecombo"])[6]').click()

    with allure.step("Seleccionar adicional Coca 1.5L y dos Coca 1/2L"):
        driver.find_element(AppiumBy.XPATH, '(//android.widget.CheckBox[@resource-id="pe.restaurant.apprestaurant:id/cb_adicionalcombo"])[1]').click()
        driver.find_element(AppiumBy.XPATH, '(//android.widget.CheckBox[@resource-id="pe.restaurant.apprestaurant:id/cb_adicionalcombo"])[2]').click()
        driver.find_element(AppiumBy.XPATH, '(//android.widget.LinearLayout[@resource-id="pe.restaurant.apprestaurant:id/ly_plus"])[2]/android.widget.ImageView').click()

    with allure.step("Agregar pedido de Criollos"):
        driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/confirm_button").click()

    with allure.step("Ver pedidos"):
        driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/btn_ver_pedidos").click()
    
    with allure.step("Agrupar pedidos"):
        driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/btn_agrupar").click()
    
    time.sleep(5)

    with allure.step("Cobrar pedido"):
        driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/btn_continuar").click()

