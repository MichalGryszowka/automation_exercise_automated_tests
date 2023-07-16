from pages.view_cart_page import ViewCart
from technical import locators
from technical.user_model import User


def test_case_10_verify_subscription_cart_page(get_main_page):

    main_page = get_main_page

    # Verify that home page is visible successfully
    assert main_page.check_el_visibility(locators.Main.main_slider_locator) is True

    view_cart_page = main_page.click_button(locators.Main.cart_button_locator, ViewCart)

    view_cart_page.scroll_page_down()

    # Verify text 'SUBSCRIPTION'
    assert view_cart_page.get_text_2(locators.ViewCart.subscription_locator) == "SUBSCRIPTION"

    view_cart_page.fill_in_data(locators.ViewCart.subscription_mail_locator, User.email)

    view_cart_page.click_button(locators.ViewCart.subscription_button_locator, ViewCart)

    # Verify success message 'You have been successfully subscribed!' is visible
    assert view_cart_page.get_text(locators.Main.subscription_success_msg) == 'You have been successfully subscribed!'
