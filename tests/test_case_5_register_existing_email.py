from pages.login_page import LoginPage
from technical import locators
from technical.user_model import User


def test_case_5_register_existing_email(get_main_page):

    main_page = get_main_page

    # Verify that home page is visible successfully
    assert main_page.check_el_visibility(locators.Main.main_slider_locator) is True

    login_page = main_page.click_button(locators.Main.login_locator, LoginPage)

    # Verify 'New User Signup!' is visible
    assert login_page.get_text(locators.Login.new_user_signup_locator) == 'New User Signup!'

    login_page.fill_in_data(locators.Login.new_user_name_locator, User.name)

    login_page.fill_in_data(locators.Login.new_user_email_locator, User.existing_email)

    login_page.click_button(locators.Login.signup_button_locator, LoginPage)

    assert login_page.get_text(locators.Login.email_already_exist) == 'Email Address already exist!'


