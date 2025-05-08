from appium import webdriver
from appium.options.android import UiAutomator2Options

def start_appium_driver():
    options = UiAutomator2Options()
    options.set_capability("platformName", "Android")
    options.set_capability("deviceName", "Galaxy A16")
    options.set_capability("automationName", "UiAutomator2")
    options.set_capability("app", "D:\\descargas\\base.apk")
    options.set_capability("autoGrantPermissions", True)

    driver = webdriver.Remote(command_executor="http://127.0.0.1:4723", options=options)
    driver.implicitly_wait(10)
    return driver
