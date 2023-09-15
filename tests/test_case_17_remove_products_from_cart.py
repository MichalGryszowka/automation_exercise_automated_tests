from pages.products_page import ProductsPage
from pages.view_cart_page import ViewCartPage
from technical import locators


def test_case_17_remove_products_from_cart(get_main_page):

    main_page = get_main_page

    # Verify that home page is visible successfully
    assert main_page.check_el_visibility(locators.Main.main_slider_locator) is True

    products_page = main_page.click_button(locators.Main.product_button_locator, ProductsPage)

    products_page.scroll_page_down(300)

    products_page.hover_cursor(locators.Products.hover_first_product_locator)

    products_page.click_element(locators.Products.add_to_cart_first_product)

    products_page.wait_and_click(locators.Products.continue_shopping_button_locator, 2, ProductsPage)

    products_page.hover_cursor(locators.Products.hover_second_product_locator)

    products_page.click_element(locators.Products.add_to_cart_second_product)

    view_cart_page = products_page.wait_and_click(locators.Products.view_cart_locator, 2, ViewCartPage)

    # Verify cart page is displayed
    assert view_cart_page.get_url() == 'https://automationexercise.com/view_cart'

    view_cart_page.click_element(locators.ViewCart.delete_x_button_first_product)

    view_cart_page.click_element(locators.ViewCart.delete_x_button_second_product)

    # Verify that products are removed from the cart
    assert view_cart_page.get_text(locators.ViewCart.cart_is_empty_msg) == 'Cart is empty!'
