from Base import Actions, Locators


class MainPage(Actions):
    def click_element(self, locator):
        self.find_element(locator).click()

    def get_element_text(self, locator):
        return self.find_element(locator).text

    def keyboard_search(self):
        self.driver.execute_script('mobile: performEditorAction', {'action': 'search'})

    def enter_text(self, locator, text):
        self.find_element(locator).send_keys(text)

    def sort_by(self, By):
        self.click_element(Locators.SORT_BUTTON)
        if By is 'popularity':
            self.click_element(Locators.POPULARITY)
        elif By is 'rating':
            self.click_element(Locators.RATING)
        elif By is 'price_min':
            self.click_element(Locators.PRICE_MIN)
        elif By is 'price_max':
            self.click_element(Locators.PRICE_MAX)
        elif By is 'update':
            self.click_element(Locators.UPDATE)
        elif By is 'discount':
            self.click_element(Locators.DISC)

    @staticmethod
    def check_titles_unique(first_title, second_title):
        assert first_title != second_title, 'BANNER NOT SWIPED'
