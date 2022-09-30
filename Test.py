import time
import appium.webdriver.extensions.keyboard
from appium.webdriver.common.touch_action import TouchAction
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from Base import Actions, Locators


def test_scroll(browser):
    launcher = Actions(browser)
    # launcher.swipe_element('down', Locators.MAIN_MENU_LIST)
    launcher.find_element(Locators.RUSSIA_SELECTOR).click()
    launcher.find_element(Locators.SKIP_BUTTON).click()
    launcher.find_element(Locators.MAIN_BANNER).click()
    text1 = launcher.find_element(Locators.TOOLBAR_TITLE).text
    launcher.find_element(Locators.TAB_BAR_MAIN).click()
    launcher.swipe_element('left', Locators.MAIN_BANNER)
    launcher.find_element(Locators.MAIN_BANNER).click()
    text2 = launcher.find_element(Locators.TOOLBAR_TITLE).text
    assert text1 != text2
    # launcher.find_element(Locators.TAB_BAR_CATALOGUE).click()
    # search = launcher.find_element(Locators.SEARCH)
    # search.click()
    # search_a = launcher.find_element(Locators.SEARCH_A)
    # search_a.send_keys('T-shirt')
    # launcher.driver.execute_script('mobile: performEditorAction', {'action': 'search'})
    # launcher.find_element(Locators.FILTER).click()
    # launcher.find_element(Locators.CATEGORY).click()
    # while launcher.is_present(Locators.POLO) is False:
    #     try:
    #         launcher.find_element(Locators.POLO).click()
    #     except:
    #         launcher.swipe_element('up', Locators.FILTER_AREA)
    #launcher.swipe_element('down', Locators.FILTER_AREA)
    time.sleep(3)
    #launcher.swipe('left', Locators.MAIN_MENU_BANNER)
