import pytest
from appium import webdriver
from pages.Base import BaseLocators, Actions


@pytest.fixture(scope='session')
def browser():
    capability = {
            "platformName": "Android",
            "platformVersion": "11",
            "udid": "emulator-5554",
            "app": "/home/mmonk3/PycharmProjects/Simbirsoft_test_task/Wildberries_4.8.3000.apk",
            "appPackage": "com.wildberries.ru",
            "appActivity": "ru.wildberries.SplashActivity"
    }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=capability)
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def setup(browser):
    region_select_page = Actions(browser)
    region_select_page.click_element(BaseLocators.RUSSIA_SELECTOR)
    region_select_page.click_element(BaseLocators.SKIP_BUTTON)
    yield browser
