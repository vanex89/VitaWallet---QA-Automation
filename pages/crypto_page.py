
from appium.webdriver.common.appiumby import AppiumBy

class CryptoPage:
    def __init__(self, driver):
        self.driver = driver
        # TODO: Reemplazar placeholders con locators capturados en Inspector (según build)
        self.menu_cripto = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Cripto")')
        self.origen_ars = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("ARS")')
        self.destino_usdt = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("USDT")')
        self.input_monto = (AppiumBy.XPATH, '//android.widget.EditText')  # ajustar si hay varios
        self.btn_confirmar = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Confirm")')

    def ir_a_cripto(self):
        self.driver.find_element(*self.menu_cripto).click()

    def seleccionar_origen_ars(self):
        self.driver.find_element(*self.origen_ars).click()

    def seleccionar_destino_usdt(self):
        self.driver.find_element(*self.destino_usdt).click()

    def ingresar_monto(self, valor: str):
        self.driver.find_element(*self.input_monto).send_keys(valor)

    def confirmar(self):
        self.driver.find_element(*self.btn_confirmar).click()
