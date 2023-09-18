from technical import locators


def test_case_18_view_category_products(get_main_page):

    main_page = get_main_page

    # Verify that home page is visible successfully
    assert main_page.check_el_visibility(locators.Main.category_products) is True

    main_page.scroll_page_down(400)

    main_page.click_element(locators.Main.woman_category)

    main_page.click_element(locators.Main.woman_category_dress)

    main_page.switch_to_default_and_refresh()

    main_page.click_element(locators.Main.woman_category)

    main_page.click_element(locators.Main.woman_category_dress)

    # Verify that category page is displayed and confirm text 'WOMEN - TOPS PRODUCTS'
    assert main_page.get_text_2(locators.Main.dress_products_title) == 'WOMEN - DRESS PRODUCTS'

    main_page.click_element(locators.Main.man_category)

    # Verify that user is navigated to that category page
    assert main_page.get_text_2(locators.Main.tshirts_products_title) == 'Sleeveless Dress'
