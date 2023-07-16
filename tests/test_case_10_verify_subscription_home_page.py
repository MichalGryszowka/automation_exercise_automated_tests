from pages.main_page import MainPage
from pages.products_page import ProductsPage
from technical import locators
from technical.user_model import User


def test_case_10_verify_subscription_home_page(get_main_page):

    main_page = get_main_page

    # Verify that home page is visible successfully
    assert main_page.check_el_visibility(locators.Main.main_slider_locator) is True

    main_page.scroll_page_down()

    # Verify text 'SUBSCRIPTION'
    assert main_page.get_text_2(locators.Main.subscription_locator) == "SUBSCRIPTION"

    main_page.fill_in_data(locators.Main.subscription_mail_locator, User.email)

    main_page.click_button(locators.Main.subscription_button_locator, MainPage)

    # Verify success message 'You have been successfully subscribed!' is visible
    assert main_page.get_text(locators.Main.subscription_success_msg) == 'You have been successfully subscribed!'
