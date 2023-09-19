from pages.products_page import ProductsPage
from technical import locators


def test_case_25_verify_scroll_up_using_arrow(get_main_page):
    main_page = get_main_page

    # Verify that home page is visible successfully
    assert main_page.check_el_visibility(locators.Main.main_slider_locator) is True

    products_page = main_page.click_button(locators.Main.product_button_locator, ProductsPage)

    products_page.scroll_page_down(9000)

    assert products_page.check_el_visibility(locators.Products.subscription_locator) is True

    products_page.click_element(locators.Products.arrow_up)

    #  Verify that page is scrolled up and 'Automation excercise frame'
    assert products_page.check_el_visibility(locators.Products.automation_excercise_frame) is True






