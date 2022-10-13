from Base import Locators


def test_scroll(setup):
    main_page = setup
    main_page.click_element(Locators.MAIN_BANNER)
    first_banner_title = main_page.get_element_text(Locators.TOOLBAR_TITLE)
    main_page.click_element(Locators.TAB_BAR_MAIN)
    main_page.swipe_element('left', Locators.MAIN_BANNER)
    main_page.click_element(Locators.MAIN_BANNER)
    second_banner_title = main_page.get_element_text(Locators.TOOLBAR_TITLE)
    main_page.click_element(Locators.TAB_BAR_MAIN)
    main_page.check_titles_unique(first_banner_title, second_banner_title)


def test_sorting(setup):
    main_page = setup
    main_page.click_element(Locators.TAB_BAR_CATALOGUE)
    main_page.click_element(Locators.SEARCH)
    main_page.enter_text(Locators.SEARCH_A, 'T-shirt')
    main_page.keyboard_search()
    main_page.sort_by('price_min')
    main_page.swipe_element('up', Locators.CATALOGUE)
    items = main_page.get_item_param(Locators.PRICE_TEXT)
    main_page.check_sort(items, 'ascending')

