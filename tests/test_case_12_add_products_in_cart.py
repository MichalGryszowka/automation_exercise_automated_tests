from pages.products_page import ProductsPage
from pages.view_cart_page import ViewCartPage
from technical import locators


def test_case_12_add_products_in_cart(get_main_page):

    main_page = get_main_page

    # Verify that home page is visible successfully
    assert main_page.check_el_visibility(locators.Main.main_slider_locator) is True

    main_page.click_button(locators.Main.product_button_locator, ProductsPage)

    main_page.switch_to_default_and_refresh()

    products_page = main_page.click_button(locators.Main.product_button_locator, ProductsPage)

    products_page.scroll_page_down(300)

    products_page.hover_cursor(locators.Products.hover_first_product_locator)

    products_page.click_element(locators.Products.add_to_cart_first_product)

    products_page.wait_and_click(locators.Products.continue_shopping_button_locator, 2, ProductsPage)

    products_page.hover_cursor(locators.Products.hover_second_product_locator)

    products_page.click_element(locators.Products.add_to_cart_second_product)

    view_cart_page = products_page.wait_and_click(locators.Products.view_cart_locator, 2, ViewCartPage)

    # Verify first products is added to Cart
    assert view_cart_page.check_el_visibility(locators.ViewCart.first_product_in_cart_basket) is True

    # Verify second products is added to Cart
    assert view_cart_page.check_el_visibility(locators.ViewCart.second_product_in_cart_basket) is True

    price_first_product_str = view_cart_page.get_text(locators.Products.unit_price_first_product)

    # Verify price of first product
    assert price_first_product_str == 'Rs. 500'

    price_first_product_int = int(price_first_product_str[3:])

    qty_first_product = int(products_page.get_text(locators.Products.qty_first_product))

    total_price_first_product_str = products_page.get_text(locators.Products.total_price_first_product)

    total_price_first_product_int = int(total_price_first_product_str[3:])

    # Verify total price of first product
    assert price_first_product_int * qty_first_product == total_price_first_product_int

    price_second_product_str = view_cart_page.get_text(locators.Products.unit_price_second_product)

    # Verify price of second product
    assert price_second_product_str == 'Rs. 400'

    price_second_product_int = int(price_second_product_str[3:])

    qty_second_product = int(products_page.get_text(locators.Products.qty_second_product))

    total_price_second_product_str = products_page.get_text(locators.Products.total_price_second_product)

    total_price_second_product_int = int(total_price_second_product_str[3:])

    # Verify total price of second product
    assert price_second_product_int * qty_second_product == total_price_second_product_int
