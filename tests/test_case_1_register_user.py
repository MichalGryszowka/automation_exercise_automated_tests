from pages.account_created_page import AccountCreatedPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.signup_page import SignupPage
from technical import locators
from technical.user_model import User


def test_case_1_register_user(get_main_page):

    main_page = get_main_page

    # Verify that home page is visible successfully
    assert main_page.check_el_visibility(locators.Main.main_slider_locator) is True

    login_page = main_page.click_button(locators.Main.login_locator, LoginPage)

    # Verify 'New User Signup!' is visible
    assert login_page.get_text(locators.Login.new_user_signup_locator) == 'New User Signup!'

    login_page.fill_in_data(locators.Login.new_user_name_locator, User.name)

    login_page.fill_in_data(locators.Login.new_user_email_locator, User.email)

    signup_page = main_page.click_button(locators.Login.signup_button_locator, SignupPage)

    # Verify 'Enter Account Information' is visible
    assert signup_page.check_el_visibility(locators.Signup.enter_account_info_locator) is True

    signup_page.get_element(locators.Signup.gender_locator).click()

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

    # Verify 'Logged in as username' is visible
    assert main_page.get_text(locators.Main.logged_on_user) == User.name

    main_page.click_button(locators.Main.delete_account, MainPage)

    # Verify 'Account Deleted' is visible
    assert main_page.get_text(locators.Main.account_deleted) == 'ACCOUNT DELETED!'

    main_page.click_button(locators.Main.account_deleted, MainPage)
