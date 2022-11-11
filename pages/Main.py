from appium.webdriver.common.appiumby import AppiumBy

from pages.Base import Actions, BaseLocators


class MainPage(Actions):
    class Locators(BaseLocators):
        MAIN_LIST = (AppiumBy.ID, 'com.wildberries.ru:id/swipeRefresh')
        MAIN_BANNER = (AppiumBy.ID, 'com.wildberries.ru:id/carousel')
        SEARCH = (AppiumBy.ID, 'com.wildberries.ru:id/search_searchEditText')
        SEARCH_TEXT_AREA = (AppiumBy.XPATH, "//*[@class='android.widget.EditText' and not (contains(@resource-id, "
                                            "'com.wildberries.ru:id/search_searchEditText'))]")
        TOOLBAR_TITLE = (AppiumBy.ID, 'com.wildberries.ru:id/toolbarTitle')
        SWIPE = (AppiumBy.ID, 'com.wildberries.ru:id/mainContentRoot')
        SORT_BUTTON = (AppiumBy.ID, 'com.wildberries.ru:id/sortButton')
        POPULARITY = (
        AppiumBy.XPATH, '//*[@resource-id="com.wildberries.ru:id/tvTitle" and (contains(@text, "популярн"))]')
        RATING = (AppiumBy.XPATH, '//*[@resource-id="com.wildberries.ru:id/tvTitle" and (contains(@text, "рейтинг"))]')
        PRICE_MIN = (AppiumBy.XPATH, '//*[@resource-id="com.wildberries.ru:id/tvTitle" and (contains(@text, "min"))]')
        PRICE_MAX = (AppiumBy.XPATH, '//*[@resource-id="com.wildberries.ru:id/tvTitle" and (contains(@text, "max"))]')
        UPDATE = (AppiumBy.XPATH, '//*[@resource-id="com.wildberries.ru:id/tvTitle" and (contains(@text, "обнов"))]')
        DISC = (AppiumBy.XPATH, '//*[@resource-id="com.wildberries.ru:id/tvTitle" and (contains(@text, "скидк"))]')
        CATALOGUE = (AppiumBy.ID, 'com.wildberries.ru:id/recyclerCatalog')
        DISC_TEXT = (AppiumBy.ID, 'com.wildberries.ru:id/textDiscount')
        PRICE_TEXT = (AppiumBy.ID, 'com.wildberries.ru:id/textBottomPrice')
        RATING_TEXT = (AppiumBy.ID, 'com.wildberries.ru:id/rating')

    def get_element_text(self, locator) -> str:
        return self.find_element(locator).text

    def keyboard_search(self) -> None:
        self.driver.execute_script('mobile: performEditorAction', {'action': 'search'})

    def enter_text(self, locator, text) -> None:
        self.find_element(locator).send_keys(text)

    def sort_by(self, By) -> None:
        self.click_element(MainPage.Locators.SORT_BUTTON)
        if By is 'popularity':
            self.click_element(MainPage.Locators.POPULARITY)
        elif By is 'rating':
            self.click_element(MainPage.Locators.RATING)
        elif By is 'price_min':
            self.click_element(MainPage.Locators.PRICE_MIN)
        elif By is 'price_max':
            self.click_element(MainPage.Locators.PRICE_MAX)
        elif By is 'update':
            self.click_element(MainPage.Locators.UPDATE)
        elif By is 'discount':
            self.click_element(MainPage.Locators.DISC)

    @staticmethod
    def check_titles_unique(first_title: str, second_title: str):
        assert first_title != second_title, 'BANNER NOT SWIPED'

    @staticmethod
    def check_sort(array, trend):
        if trend is 'ascending':
            assert all([x <= y for x, y in zip(array, array[1:])]), 'INCORRECT SORTING'
        elif trend is 'descending':
            assert all([x >= y for x, y in zip(array, array[1:])]), 'INCORRECT SORTING'
