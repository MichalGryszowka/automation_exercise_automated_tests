from pages.account_created_page import AccountCreatedPage
from pages.checkout_page import CheckoutPage
from pages.delete_account_page import DeleteAccountPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.products_page import ProductsPage
from pages.signup_page import SignupPage
from pages.view_cart_page import ViewCartPage
from technical import locators
from technical.user_model import User


def test_case_23_verify_details_in_checkout(get_main_page):

    main_page = get_main_page

    # Verify that home page is visible successfully
    assert main_page.check_el_visibility(locators.Main.main_slider_locator) is True

    login_page = main_page.click_button(locators.Main.login_locator, LoginPage)

    login_page.fill_in_data(locators.Login.new_user_name_locator, User.name)

    login_page.fill_in_data(locators.Login.new_user_email_locator, User.email)

    signup_page = main_page.click_button(locators.Login.signup_button_locator, SignupPage)

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

    # Verify 'Account Created!' is visible
    assert account_created_page.get_text(locators.AccountCreated.account_created_locator) == 'Account Created!'

    main_page = account_created_page.click_button(locators.AccountCreated.continue_locator, MainPage)

    # Verify 'Logged in as username' is visible
    assert main_page.get_text(locators.Main.logged_on_user) == 'Tomasz'

    products_page = main_page.click_button(locators.Main.product_button_locator, ProductsPage)

    products_page.scroll_page_down(300)

    products_page.hover_cursor(locators.Products.hover_first_product_locator)

    products_page.click_element(locators.Products.add_to_cart_first_product)

    products_page.wait_and_click(locators.Products.continue_shopping_button_locator, 2, ProductsPage)

    products_page.hover_cursor(locators.Products.hover_second_product_locator)

    products_page.click_element(locators.Products.add_to_cart_second_product)

    view_cart_page = products_page.wait_and_click(locators.Products.view_cart_locator, 2, ViewCartPage)

    # Verify cart page is displayed
    assert view_cart_page.get_url() == 'https://automationexercise.com/view_cart'

    checkout_page = view_cart_page.click_button(locators.ViewCart.proceed_to_checkout_btn, CheckoutPage)

    assert checkout_page.check_el_visibility(locators.Checkout.address_details) is True

    assert checkout_page.check_el_visibility(locators.Checkout.review_your_order) is True

    delete_account = checkout_page.click_button(locators.Checkout.delete_account, DeleteAccountPage)

    # Verify 'Account deleted' message
    assert delete_account.get_text(locators.DeleteAccount.account_deleted_locator) == 'Account Deleted!'