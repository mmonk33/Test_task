from Base import Actions


class MainPage(Actions):
    def click_element(self, locator):
        return self.find_element(locator).click()

    def get_element_text(self, locator):
        return self.find_element(locator).text

    def keyboard_search(self):
        return self.driver.execute_script('mobile: performEditorAction', {'action': 'search'})

    def enter_text(self, locator, text):
        return self.find_element(locator).send_keys(text)
