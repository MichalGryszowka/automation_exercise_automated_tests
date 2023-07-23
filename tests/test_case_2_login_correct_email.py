from pages.account_created_page import AccountCreatedPage
from pages.delete_account_page import DeleteAccountPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.signup_page import SignupPage
from technical import locators
from technical.user_model import User


def test_case_2_login_correct(get_main_page):

    main_page = get_main_page

    # Verify that home page is visible successfully
    assert main_page.check_el_visibility(locators.Main.main_slider_locator) is True

    login_page = main_page.click_button(locators.Main.login_locator, LoginPage)

    # Verify 'Login to your account' is visible
    assert login_page.get_text(locators.Login.login_to_your_account) == 'Login to your account'

    login_page.fill_in_data(locators.Login.new_user_name_locator, User.name)

    login_page.fill_in_data(locators.Login.new_user_email_locator, User.email)

    signup_page = login_page.click_button(locators.Login.signup_button_locator, SignupPage)

    signup_page.wait_and_click(locators.Signup.gender_locator, 2, SignupPage)

    signup_page.fill_in_data(locators.Signup.password_locator, User.password)

    signup_page.select_dropdown(locators.Signup.day_locator, User.day)

    signup_page.select_dropdown(locators.Signup.month_locator, User.month)

    signup_page.select_dropdown(locators.Signup.year_locator, User.year)

    signup_page.get_element(locators.Signup.newsletter_locator).click()

    signup_page.get_element(locators.Signup.special_offer_locator).click()

    signup_page.fill_in_data(locators.Signup.first_name_locator, User.name)

    signup_page.fill_in_data(locators.Signup.last_name_locator, User.surname)

    signup_page.fill_in_data(locators.Signup.company_locator, User.company)

    signup_page.fill_in_data(locators.Signup.address1_locator, User.address1)

    signup_page.fill_in_data(locators.Signup.address2_locator, User.address2)

    signup_page.select_dropdown(locators.Signup.country_locator, User.country)

    signup_page.fill_in_data(locators.Signup.state_locator, User.address2)

    signup_page.fill_in_data(locators.Signup.city_locator, User.address2)

    signup_page.fill_in_data(locators.Signup.zipcode_locator, User.zipcode)

    signup_page.fill_in_data(locators.Signup.mobile_number_locator, User.mobile)

    account_created_page = signup_page.click_button(locators.Signup.create_account_button, AccountCreatedPage)

    account_created_page.click_button(locators.AccountCreated.continue_locator, MainPage)

    account_created_page.switch_to_default_and_refresh()

    main_page = account_created_page.click_button(locators.AccountCreated.continue_locator, MainPage)

    login_page = main_page.click_button(locators.Main.login_locator, LoginPage)

    login_page.fill_in_data(locators.Login.existing_email, User.email)

    login_page.fill_in_data(locators.Login.existing_password, User.password)

    main_page = login_page.click_button(locators.Login.login_button_locator, MainPage)

    # Verify 'Logged in as username' is visible
    assert main_page.get_text(locators.Main.logged_on_user) == 'Tomasz'

    account_deleted_page = main_page.click_button(locators.Main.delete_account, DeleteAccountPage)

    account_deleted_page.switch_to_default_and_refresh()

    # Verify 'Account Deleted' is visible
    assert main_page.get_text(locators.DeleteAccount.account_deleted_locator) == 'Account Deleted!'

