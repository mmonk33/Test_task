from Base import Locators
from Main import MainPage


def test_scroll(browser):
    main_page = MainPage(browser)
    main_page.click_element(Locators.RUSSIA_SELECTOR)
    main_page.click_element(Locators.SKIP_BUTTON)
    main_page.click_element(Locators.MAIN_BANNER)
    first_banner_title = main_page.get_element_text(Locators.TOOLBAR_TITLE)
    main_page.click_element(Locators.TAB_BAR_MAIN)
    main_page.swipe_element('left', Locators.MAIN_BANNER)
    main_page.click_element(Locators.MAIN_BANNER)
    second_banner_title = main_page.get_element_text(Locators.TOOLBAR_TITLE)
    main_page.click_element(Locators.TAB_BAR_MAIN)
    assert first_banner_title != second_banner_title, 'BANNER NOT SWIPED'


def test_sorting(browser):
    main_page = MainPage(browser)
    main_page.click_element(Locators.TAB_BAR_CATALOGUE)
    main_page.click_element(Locators.SEARCH)
    main_page.enter_text(Locators.SEARCH_A, 'T-shirt')
    main_page.keyboard_search()
    main_page.sort_by('price_min')
    items = main_page.get_item_param(Locators.PRICE_TEXT)
    assert main_page.check_sort(items, 'ascending'), 'INCORRECT SORTING'

