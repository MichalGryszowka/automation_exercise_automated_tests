from pages.product_details_1_page import ProductsDetails1Page
from pages.view_cart_page import ViewCartPage
from technical import locators


def test_case_13_verify_product_quantity_in_cart(get_main_page):

    main_page = get_main_page

    # Verify that home page is visible successfully
    assert main_page.check_el_visibility(locators.Main.main_slider_locator) is True

    main_page.scroll_page_down(100)

    product_1_details = main_page.click_button(locators.Main.view_first_product, ProductsDetails1Page)

    # Verify product detail is opened
    assert product_1_details.get_url() == 'https://automationexercise.com/product_details/1'

    product_1_details.get_element(locators.Products.dynamic_qty_first_product).clear()

    product_1_details.fill_in_data(locators.Products.dynamic_qty_first_product, '4')

    product_1_details.click_element(locators.Products.to_cart_first_product)

    view_cart_page = product_1_details.wait_and_click(locators.Products.view_cart_locator, 2, ViewCartPage)

    qty_first_product = int(view_cart_page.get_text(locators.Products.qty_first_product))

    # verify product is displayed in cart with exact quantity
    assert qty_first_product == 4


