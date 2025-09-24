
import os
import pytest
from appium.webdriver.common.appiumby import AppiumBy
from pages.login_page import LoginPage

USER = os.getenv("VITA_USER", "derly+qa02@vitawallet.io")
PASS = os.getenv("VITA_PASS", "vitawallet")

@pytest.mark.smoke
@pytest.mark.login
def test_login_valido(driver):
    # Ir a 'Iniciar sesión' desde onboarding si aplica
    if "Iniciar sesión" in driver.page_source:
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                            'new UiSelector().text("Iniciar sesión")').click()

    page = LoginPage(driver)
    page.type_email(USER)
    page.type_password(PASS)
    page.tap_ingresar()

    # Assert básico: presencia de elementos del Home (ajustar al locator real)
    assert ("Cripto" in driver.page_source) or ("Inicio" in driver.page_source)
