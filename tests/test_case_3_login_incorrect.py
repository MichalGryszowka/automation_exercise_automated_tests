from pages.login_page import LoginPage
from technical import locators
from technical.user_model import User


def test_case_3_login_incorrect(get_main_page):

    main_page = get_main_page

    # Verify that home page is visible successfully
    assert main_page.check_el_visibility(locators.Main.main_slider_locator) is True

    login_page = main_page.click_button(locators.Main.login_locator, LoginPage)

    # Verify 'Login to your account' is visible
    assert login_page.get_text(locators.Login.login_to_your_account) == 'Login to your account'

    login_page.fill_in_data(locators.Login.existing_email, User.email)

    login_page.fill_in_data(locators.Login.existing_password, User.password)

    login_page.click_button(locators.Login.login_button_locator, LoginPage)

    assert login_page.get_text(locators.Login.email_incorrect_locator) == 'Your email or password is incorrect!'

