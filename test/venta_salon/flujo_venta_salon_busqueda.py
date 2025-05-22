import time
import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def venta_por_salon_busqueda(driver):
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
           
    with allure.step("busqueda de productos"):   
        campo_busqueda = WebDriverWait(driver, 10).until(
         EC.presence_of_element_located((AppiumBy.ID, "pe.restaurant.apprestaurant:id/search_src_text"))
         )
        campo_busqueda.clear()
        campo_busqueda.set_value("combo")  
        
        driver.find_element(AppiumBy.XPATH, '(//android.widget.Button[@resource-id="pe.restaurant.apprestaurant:id/bt_agregar"])[1]').click()
        driver.find_element(AppiumBy.XPATH, '(//android.widget.RadioButton[@resource-id="pe.restaurant.apprestaurant:id/rb_detallecombo"])[2]').click()
        driver.find_element(AppiumBy.XPATH, '(//android.widget.RadioButton[@resource-id="pe.restaurant.apprestaurant:id/rb_detallecombo"])[4]').click()
        driver.find_element(AppiumBy.XPATH, '(//android.widget.CheckBox[@resource-id="pe.restaurant.apprestaurant:id/cb_adicionalcombo"])[1]').click()
        plus_button = driver.find_element(AppiumBy.XPATH, '(//android.widget.LinearLayout[@resource-id="pe.restaurant.apprestaurant:id/ly_plus"])[1]')
        plus_button.click()
        plus_button.click()  
        driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/confirm_button").click()   
        driver.find_element(AppiumBy.XPATH, '//android.widget.LinearLayout[@resource-id="pe.restaurant.apprestaurant:id/ly_back"]/android.widget.ImageView').click()   
        driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="pe.restaurant.apprestaurant:id/text_name_categoria" and @text="Criollos"]').click() 
        driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/text_name_productogeneral").click()
        driver.find_element(AppiumBy.XPATH, '(//android.widget.RadioButton[@resource-id="pe.restaurant.apprestaurant:id/rb_detallecombo"])[2]').click()
        driver.find_element(AppiumBy.XPATH, '(//android.widget.RadioButton[@resource-id="pe.restaurant.apprestaurant:id/rb_detallecombo"])[4]').click()
        driver.find_element(AppiumBy.XPATH, '(//android.widget.RadioButton[@resource-id="pe.restaurant.apprestaurant:id/rb_detallecombo"])[6]').click()  
        driver.find_element(AppiumBy.XPATH, '(//android.widget.CheckBox[@resource-id="pe.restaurant.apprestaurant:id/cb_adicionalcombo"])[1]').click()
        driver.find_element(AppiumBy.XPATH, '(//android.widget.CheckBox[@resource-id="pe.restaurant.apprestaurant:id/cb_adicionalcombo"])[2]').click()
        driver.find_element(AppiumBy.XPATH, '(//android.widget.LinearLayout[@resource-id="pe.restaurant.apprestaurant:id/ly_plus"])[2]/android.widget.ImageView').click()  
        driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/confirm_button").click()   
        driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/btn_ver_pedidos").click()  
        driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/btn_agrupar").click()  
        time.sleep(5) 
        
            #COBRAR PEDIDO
        driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/btn_continuar").click()