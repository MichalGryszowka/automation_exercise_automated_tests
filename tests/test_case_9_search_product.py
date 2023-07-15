from pages.products_page import ProductsPage
from technical import locators
from technical.user_model import User


def test_case_9_search_product(get_main_page):

    main_page = get_main_page

    # Verify that home page is visible successfully
    assert main_page.check_el_visibility(locators.Main.main_slider_locator) is True

    main_page.click_button(locators.Products.product_button_locator, ProductsPage)

    main_page.switch_to_default_and_refresh()

    products_page = main_page.click_button(locators.Products.product_button_locator, ProductsPage)

    # Verify user is navigated to ALL PRODUCTS page successfully
    assert products_page.get_url() == 'https://automationexercise.com/products'

    products_page.fill_in_data(locators.Products.search_product_locator, User.product_name)

    products_page.click_button(locators.Products.loop_locator, ProductsPage)

    # Verify 'SEARCHED PRODUCTS' is visible
    assert products_page.check_el_visibility(locators.Products.search_product_locator) is True

    # Verify all the products related to search are visible
    assert products_page.get_text(locators.Products.searched_blue_top) == 'Blue Top'











