import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.feature("Venta rápida")
@allure.story("Búsqueda y selección de combos")
def venta_rapida_busqueda(driver):

    @allure.step("Ir a la sección Vender")
    def ir_a_vender():
        venderclick = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.LinearLayout[@resource-id="pe.restaurant.apprestaurant:id/ll_vender"]'))
        )
        venderclick.click()
        screenshot = driver.get_screenshot_as_png()
        allure.attach(screenshot, name="Pantalla Sección Vender", attachment_type=allure.attachment_type.PNG)
        allure.attach("Se hizo clic en la sección Vender para iniciar el proceso.", name="Descripción paso", attachment_type=allure.attachment_type.TEXT)

    @allure.step("Seleccionar Venta rápida")
    def seleccionar_venta_rapida():
        driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/btn_venta_rapida").click()
        screenshot = driver.get_screenshot_as_png()
        allure.attach(screenshot, name="Pantalla Venta Rápida", attachment_type=allure.attachment_type.PNG)
        allure.attach("Se seleccionó la opción Venta rápida.", name="Descripción paso", attachment_type=allure.attachment_type.TEXT)

    @allure.step("Click en búsqueda")
    def click_en_busqueda():
        driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/tv_busqueda").click()
        screenshot = driver.get_screenshot_as_png()
        allure.attach(screenshot, name="Pantalla Búsqueda", attachment_type=allure.attachment_type.PNG)
        allure.attach("Se hizo clic en el campo de búsqueda.", name="Descripción paso", attachment_type=allure.attachment_type.TEXT)

    @allure.step("Escribir texto en campo de búsqueda")
    def escribir_busqueda(texto):
        campo_busqueda = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "pe.restaurant.apprestaurant:id/search_src_text"))
        )
        campo_busqueda.clear()
        campo_busqueda.set_value(texto)
        screenshot = driver.get_screenshot_as_png()
        allure.attach(screenshot, name=f"Campo búsqueda con texto '{texto}'", attachment_type=allure.attachment_type.PNG)
        allure.attach(f"Se escribió '{texto}' en el campo de búsqueda.", name="Descripción paso", attachment_type=allure.attachment_type.TEXT)

    @allure.step("Agregar primer combo de la lista")
    def agregar_primer_combo():
        driver.find_element(AppiumBy.XPATH, '(//android.widget.Button[@resource-id="pe.restaurant.apprestaurant:id/bt_agregar"])[1]').click()
        screenshot = driver.get_screenshot_as_png()
        allure.attach(screenshot, name="Agregar primer combo", attachment_type=allure.attachment_type.PNG)
        allure.attach("Se agregó el primer combo de la lista.", name="Descripción paso", attachment_type=allure.attachment_type.TEXT)

    @allure.step("Seleccionar tamaños para combo")
    def seleccionar_tamanos(*indices):
        for idx in indices:
            driver.find_element(AppiumBy.XPATH, f'(//android.widget.RadioButton[@resource-id="pe.restaurant.apprestaurant:id/rb_detallecombo"])[{idx}]').click()
        screenshot = driver.get_screenshot_as_png()
        allure.attach(screenshot, name="Tamaños seleccionados", attachment_type=allure.attachment_type.PNG)
        allure.attach(f"Se seleccionaron los tamaños con índices: {indices}.", name="Descripción paso", attachment_type=allure.attachment_type.TEXT)

    @allure.step("Seleccionar adicionales para combo")
    def seleccionar_adicionales(*indices):
        for idx in indices:
            driver.find_element(AppiumBy.XPATH, f'(//android.widget.CheckBox[@resource-id="pe.restaurant.apprestaurant:id/cb_adicionalcombo"])[{idx}]').click()
        screenshot = driver.get_screenshot_as_png()
        allure.attach(screenshot, name="Adicionales seleccionados", attachment_type=allure.attachment_type.PNG)
        allure.attach(f"Se seleccionaron adicionales con índices: {indices}.", name="Descripción paso", attachment_type=allure.attachment_type.TEXT)

    @allure.step("Aumentar cantidad adicional seleccionado")
    def aumentar_cantidad_adicional(veces, index=1):
        for _ in range(veces):
            plus_button = driver.find_element(AppiumBy.XPATH, f'(//android.widget.LinearLayout[@resource-id="pe.restaurant.apprestaurant:id/ly_plus"])[{index}]')
            plus_button.click()
        screenshot = driver.get_screenshot_as_png()
        allure.attach(screenshot, name="Cantidad adicional aumentada", attachment_type=allure.attachment_type.PNG)
        allure.attach(f"Se aumentó la cantidad del adicional índice {index} en {veces} veces.", name="Descripción paso", attachment_type=allure.attachment_type.TEXT)

    @allure.step("Confirmar selección")
    def confirmar_seleccion():
        driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/confirm_button").click()
        screenshot = driver.get_screenshot_as_png()
        allure.attach(screenshot, name="Confirmación selección", attachment_type=allure.attachment_type.PNG)
        allure.attach("Se confirmó la selección de combos y adicionales.", name="Descripción paso", attachment_type=allure.attachment_type.TEXT)

    @allure.step("Volver a la pantalla principal")
    def volver_principal():
        driver.find_element(AppiumBy.XPATH, '//android.widget.LinearLayout[@resource-id="pe.restaurant.apprestaurant:id/ly_back"]/android.widget.ImageView').click()
        screenshot = driver.get_screenshot_as_png()
        allure.attach(screenshot, name="Pantalla principal", attachment_type=allure.attachment_type.PNG)
        allure.attach("Se volvió a la pantalla principal.", name="Descripción paso", attachment_type=allure.attachment_type.TEXT)

    @allure.step("Seleccionar categoría")
    def seleccionar_categoria(nombre_categoria):
        driver.find_element(AppiumBy.XPATH, f'//android.widget.TextView[@resource-id="pe.restaurant.apprestaurant:id/text_name_categoria" and @text="{nombre_categoria}"]').click()
        screenshot = driver.get_screenshot_as_png()
        allure.attach(screenshot, name=f"Categoría {nombre_categoria}", attachment_type=allure.attachment_type.PNG)
        allure.attach(f"Se seleccionó la categoría '{nombre_categoria}'.", name="Descripción paso", attachment_type=allure.attachment_type.TEXT)

    @allure.step("Seleccionar subcategoría")
    def seleccionar_subcategoria():
        driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/text_name_productogeneral").click()
        screenshot = driver.get_screenshot_as_png()
        allure.attach(screenshot, name="Subcategoría seleccionada", attachment_type=allure.attachment_type.PNG)
        allure.attach("Se seleccionó la subcategoría.", name="Descripción paso", attachment_type=allure.attachment_type.TEXT)

    @allure.step("Ver pedidos")
    def ver_pedidos():
        driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/btn_ver_pedidos").click()
        screenshot = driver.get_screenshot_as_png()
        allure.attach(screenshot, name="Pantalla Ver Pedidos", attachment_type=allure.attachment_type.PNG)
        allure.attach("Se accedió a la pantalla de ver pedidos.", name="Descripción paso", attachment_type=allure.attachment_type.TEXT)

    @allure.step("Enviar pedido")
    def enviar_pedido():
        driver.find_element(AppiumBy.ID, "pe.restaurant.apprestaurant:id/btn_agrupar").click()
        screenshot = driver.get_screenshot_as_png()
        allure.attach(screenshot, name="Pedido enviado", attachment_type=allure.attachment_type.PNG)
        allure.attach("Se envió el pedido correctamente.", name="Descripción paso", attachment_type=allure.attachment_type.TEXT)

    # Ejecutar el flujo completo
    ir_a_vender()
    seleccionar_venta_rapida()
    click_en_busqueda()
    escribir_busqueda("combo")
    agregar_primer_combo()
    seleccionar_tamanos(2, 4)  # Hawaiana pequeña y mediana
    seleccionar_adicionales(1)  # Pepsi 1/2 litro
    aumentar_cantidad_adicional(2, index=1)
    confirmar_seleccion()
    volver_principal()
    seleccionar_categoria("Criollos")
    seleccionar_subcategoria()
    seleccionar_tamanos(2, 4, 6)  # Lomo Saltado familiar, personal y mediano
    seleccionar_adicionales(1, 2)  # Coca 1.5L y dos Coca 1/2L
    aumentar_cantidad_adicional(1, index=2)
    confirmar_seleccion()
    ver_pedidos()
    enviar_pedido()
