from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Locators:
    MAIN_LIST = (AppiumBy.ID, 'com.wildberries.ru:id/swipeRefresh')
    MAIN_BANNER = (AppiumBy.ID, 'com.wildberries.ru:id/carousel')
    TAB_BAR_CATALOGUE = (AppiumBy.ID, 'com.wildberries.ru:id/btnCatalogue')
    SEARCH = (AppiumBy.ID, 'com.wildberries.ru:id/search_searchEditText')
    FILTER = (AppiumBy.ID, 'com.wildberries.ru:id/filterButton')
    CATEGORY = (AppiumBy.XPATH, '//*[@resource-id="com.wildberries.ru:id/tvTitle" and (contains(@text, "Категория"))]')
    SEARCH_A = (AppiumBy.XPATH, "//*[@class='android.widget.EditText' and not (contains(@resource-id, 'com.wildberries.ru:id/search_searchEditText'))]")
    FILTER_AREA = (AppiumBy.ID, 'com.wildberries.ru:id/rvFilters')
    POLO = (AppiumBy.XPATH, '//*[@resource-id="com.wildberries.ru:id/tvFilterValue" and (contains(@text, "поло"))]')
    TOOLBAR_TITLE = (AppiumBy.ID, 'com.wildberries.ru:id/toolbarTitle')
    TAB_BAR_MAIN = (AppiumBy.ID, 'com.wildberries.ru:id/btnMain')
    CAROUSEL_TEXT = (AppiumBy.XPATH, "//*[@class='android.widget.TextView'][2]")
    RUSSIA_SELECTOR = (AppiumBy.XPATH, "//*[@class='android.widget.TextView' and (contains(@text, 'Россия'))]")
    SWIPE = (AppiumBy.ID, 'com.wildberries.ru:id/mainContentRoot')
    SKIP_BUTTON = (AppiumBy.XPATH, "//*[@class='android.widget.Button']")


class Actions:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, timer=5):
        return WebDriverWait(self.driver, timer).until(EC.presence_of_element_located(locator),
                                                       message=f"Can't find element by locator {locator}")

    def swipe_element(self, direction, locator):
        element = self.find_element(locator)
        left_x = int(element.location['x']) + 10
        right_x = int(element.size['width']) - 10
        middle_x = (right_x + left_x) / 2
        upper_y = int(element.location['y']) + 10
        lower_y = int(element.size['height']) - 10
        middle_y = (upper_y + lower_y) / 2
        if direction is 'left':
            self.driver.swipe(right_x, middle_y, left_x, middle_y, 1000)
        elif direction is 'right':
            self.driver.swipe(left_x, middle_y, right_x, middle_y, 1000)
        elif direction is 'down':
            self.driver.swipe(middle_x, upper_y, left_x, lower_y, 1000)
        elif direction is 'up':
            self.driver.swipe(middle_x, lower_y, left_x, upper_y, 1000)
        else:
            print('Unknown direction')

    def is_present(self, locator):
        element = self.driver.find_elements(locator)
        if len(element) == 0:
            return False
        else:
            return True
