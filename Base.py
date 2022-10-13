from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseLocators:
    TAB_BAR_CATALOGUE = (AppiumBy.ID, 'com.wildberries.ru:id/btnCatalogue')
    TAB_BAR_MAIN = (AppiumBy.ID, 'com.wildberries.ru:id/btnMain')
    RUSSIA_SELECTOR = (AppiumBy.XPATH, "//*[@class='android.widget.TextView' and (contains(@text, 'Россия'))]")
    SKIP_BUTTON = (AppiumBy.XPATH, "//*[@class='android.widget.Button']")


class Actions:
    def __init__(self, driver):
        self.driver = driver

    def click_element(self, locator):
        self.find_element(locator).click()

    def find_element(self, locator, timer=10):
        return WebDriverWait(self.driver, timer).until(EC.element_to_be_clickable(locator),
                                                       message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, timer=10):
        return WebDriverWait(self.driver, timer).until(EC.presence_of_all_elements_located(locator),
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

    def get_item_param(self, locator):
        items = self.find_elements(locator)
        values = []
        for item in items:
            values.append(item.text)
        return values

    @staticmethod
    def check_sort(array, trend):
        if trend is 'ascending':
            assert all([x <= y for x, y in zip(array, array[1:])]), 'INCORRECT SORTING'
        elif trend is 'descending':
            assert all([x >= y for x, y in zip(array, array[1:])]), 'INCORRECT SORTING'
