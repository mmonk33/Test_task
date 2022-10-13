import pytest
from appium import webdriver

from Base import Locators
from Main import MainPage


@pytest.fixture(scope='session')
def browser():
    capability = {
            "platformName": "Android",
            "platformVersion": "11",
            "udid": "emulator-5554",
            "appPackage": "com.wildberries.ru",
            "appActivity": "ru.wildberries.SplashActivity"
    }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=capability)
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def setup(browser):
    page = MainPage(browser)
    page.click_element(Locators.RUSSIA_SELECTOR)
    page.click_element(Locators.SKIP_BUTTON)
    yield page
