from pages.login_page import LoginPage
from pages.main_page import MainPage
from technical import locators
from technical.user_model import User


def test_case_4_logout_user(get_main_page):

    main_page = get_main_page

    # Verify that home page is visible successfully
    assert main_page.check_el_visibility(locators.Main.main_slider_locator) is True

    login_page = main_page.click_button(locators.Main.login_locator, LoginPage)

    # Verify 'Login to your account' is visible
    assert login_page.get_text(locators.Login.login_to_your_account) == 'Login to your account'

    login_page.fill_in_data(locators.Login.existing_email, User.existing_email)

    login_page.fill_in_data(locators.Login.existing_password, User.password)

    main_page = login_page.click_button(locators.Login.login_button_locator, MainPage)

    # Verify 'Logged in as username' is visible
    assert main_page.get_text(locators.Main.logged_on_user) == 'Tomasz'

    login_page = main_page.click_button(locators.Main.logout_button, LoginPage)

    # Verify 'Login to your account' is visible
    assert login_page.get_text(locators.Login.login_to_your_account) == 'Login to your account'
