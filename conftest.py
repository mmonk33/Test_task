import pytest
from appium import webdriver


@pytest.fixture(scope='session', autouse=True)
def browser():
    capability = {
            "platformName": "Android",
            "platformVersion": "9",
            "udid": "emulator-5554",
            "appPackage": "com.wildberries.ru",
            "appActivity": "ru.wildberries.SplashActivity"
    }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=capability)
    yield driver
    driver.quit()