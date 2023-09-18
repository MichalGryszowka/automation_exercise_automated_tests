from pages.view_cart_page import ViewCartPage
from technical import locators


def test_case_22_add_to_cart_recommended_item(get_main_page):

    main_page = get_main_page

    main_page.scroll_page_down(7500)

    # Verify 'RECOMMENDED ITEMS' are visible
    assert main_page.get_text(locators.Main.recommended_items) == 'recommended items'

    main_page.click_element(locators.Main.add_to_cart_stylish_dress)

    view_cart_page = main_page.wait_and_click(locators.Main.view_cart_blue_top, 10, ViewCartPage)

    # Verify that product is displayed in cart page
    assert view_cart_page.check_el_visibility(locators.ViewCart.view_stylish_dress_in_basket) is True


