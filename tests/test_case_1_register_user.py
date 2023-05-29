from time import sleep
from pages.login_page import LoginPage
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

    sleep(1)
    signup_page.get_element(locators.Signup.gender_locator).click()
    sleep(1)
    signup_page.fill_in_data(locators.Signup.password_locator, User.password)
    sleep(1)
    signup_page.select_dropdown(locators.Signup.day_locator, User.day)
    sleep(1)
    signup_page.select_dropdown(locators.Signup.month_locator, User.month)
    sleep(1)
    signup_page.select_dropdown(locators.Signup.year_locator, User.year)
    sleep(1)
    signup_page.remove_advert_bar()







    # signup_page.get_element(locators.Signup.newsletter_locator).click()
    # sleep(1)
    # signup_page.get_element(locators.Signup.special_offer_locator).click()
    # sleep(1)
    # signup_page.execute_script("arguments[0].scrollIntoView();", (By.ID, 'address2'))
    # main_page.switch_to_frame(By.ID, 'aswift_4')
    # iframe = WebDriverWait(signup_page, 5).until(EC.frame_to_be_available_and_switch_to_it('aswift_2_host'))
    # sleep(1)
    # signup_register_page.fill_in_data(locators.Signup.first_name_locator, User.name)
    #
    # signup_register_page.fill_in_data(locators.Signup.last_name_locator, User.surname)
    #
    # signup_register_page.fill_in_data(locators.Signup.company_locator, User.company)
    #
    # signup_register_page.fill_in_data(locators.Signup.address1_locator, User.address1)
    #
    # signup_register_page.fill_in_data(locators.Signup.address2_locator, User.address2)
    #
    # signup_register_page.select_dropdown(locators.Signup.country_locator, User.country)
    #
    # signup_register_page.fill_in_data(locators.Signup.state_locator, User.address2)
    #
    # signup_register_page.fill_in_data(locators.Signup.city_locator, User.address2)
    #
    # signup_register_page.fill_in_data(locators.Signup.zipcode_locator, User.zipcode)
    #
    # signup_register_page.fill_in_data(locators.Signup.mobile_number_locator, User.mobile)
    #
    # signup_register_page.click_button(locators.Signup.create_account_button, AccountCreatedPage)
    #
    # # Verify 'Account created!' is visible
    # assert signup_register_page.check_el_visibility(locators.AccountCreated.account_created_locator) is True
    #
    # signup_register_page.click_button(locators.AccountCreated.continue_locator, MainPage)
    #
    # # Verify 'Logged in as username' is visible
    # assert signup_register_page.get_text(locators.MainPageLocators.logged_on_user) == User.name
    #
    # signup_register_page.click_button(locators.MainPageLocators.delete_account, DeleteAccountPage)
    #
    # # Verify 'Account deleted' is visible
    # assert signup_register_page.check_el_visibility(locators.DeleteAccount.account_deleted_locator) is True
    #
    # signup_register_page.click_button(locators.DeleteAccount.continue_button_locator, MainPage)
