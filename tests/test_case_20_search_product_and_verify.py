from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.products_page import ProductsPage
from pages.view_cart_page import ViewCartPage
from technical import locators

from technical.user_model import User


def test_case_20_search_product_and_verify(get_main_page):

    main_page = get_main_page

    products_page = main_page.click_button(locators.Main.product_button_locator, ProductsPage)

    # Verify user is navigated to ALL PRODUCTS page successfully
    assert products_page.get_url() == 'https://automationexercise.com/products'

    products_page.scroll_page_down(300)

    products_page.fill_in_data(locators.Products.search_product_locator, User.product_name)

    products_page.click_button(locators.Products.loop_locator, ProductsPage)

    # Verify 'SEARCHED PRODUCTS' is visible
    assert products_page.check_el_visibility(locators.Products.search_product_locator) is True

    products_page.hover_cursor(locators.Products.hover_first_product_locator)

    products_page.click_element(locators.Products.add_to_cart_first_product)

    view_cart_page = products_page.wait_and_click(locators.Products.view_cart_locator, 2, ViewCartPage)

    # Verify first products is added to Cart
    assert view_cart_page.check_el_visibility(locators.ViewCart.first_product_in_cart_basket) is True

    login_page = view_cart_page.wait_and_click(locators.ViewCart.signup_login, 2, LoginPage)

    login_page.fill_in_data(locators.Login.existing_email, User.existing_email)

    login_page.fill_in_data(locators.Login.existing_password, User.password)

    main_page = login_page.wait_and_click(locators.Login.login_to_your_account, 2, MainPage)

    view_cart_page = main_page.click_button(locators.Main.cart_button_locator, ViewCartPage)

    # Verify that those products are visible in cart after login as well
    assert view_cart_page.check_el_visibility(locators.ViewCart.first_product_in_cart_basket) is True