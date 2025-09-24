
import os
import pytest
from appium import webdriver
from appium.options.common import AppiumOptions

APK_PATH = os.getenv("VITA_APK", r"C:\Users\vaned\Downloads\VitaAppium\VitaQA.apk")

@pytest.fixture(scope="session")
def driver():
    options = AppiumOptions()
    options.load_capabilities({
        "platformName": "Android",
        "automationName": "UiAutomator2",
        "app": APK_PATH,
        "newCommandTimeout": 180,
        "autoGrantPermissions": True,
        "dontStopAppOnReset": False,
        "fullReset": False,
        "noReset": True
    })
    drv = webdriver.Remote("http://127.0.0.1:4723", options=options)
    yield drv
    drv.quit()
