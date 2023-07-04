from pages.delete_account_page import DeleteAccountPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from technical import locators
from technical.user_model import User
from time import sleep

def test_case_1_register_user(get_main_page):

    main_page = get_main_page

    # Verify that home page is visible successfully
    assert main_page.check_el_visibility(locators.Main.main_slider_locator) is True

    login_page = main_page.click_button(locators.Main.login_locator, LoginPage)

    # Verify 'New User Signup!' is visible
    assert login_page.get_text(locators.Login.login_to_your_account) == 'Login to your account'

    login_page.fill_in_data(locators.Login.existing_email, User.correct_email)

    login_page.fill_in_data(locators.Login.existing_password, User.password)

    main_page = login_page.click_button(locators.Login.login_button_locator, MainPage)

    # Verify 'Logged in as username' is visible
    assert main_page.get_text(locators.Main.logged_on_user) == 'Jan'

    main_page.click_button(locators.Main.delete_account, DeleteAccountPage)

    main_page.switch_to_default_and_refresh()

    # Verify 'Account Deleted' is visible
    # assert main_page.get_text(locators.DeleteAccount.account_deleted_locator) == 'Account Deleted!'

