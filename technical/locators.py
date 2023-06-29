from selenium.webdriver.common.by import By


class Main:
    main_slider_locator = (By.ID, "slider")
    login_locator = (By.XPATH, '/html/body/header/div/div/div/div[2]/div/ul/li[4]')
    logged_on_user = (By.XPATH, '/html/body/header/div/div/div/div[2]/div/ul/li[10]/a/b')
    delete_account = (By.XPATH, '/html/body/header/div/div/div/div[2]/div/ul/li[5]/a/i')
    main_page_box = (By.XPATH, '/html/body/header/div/div/div/div[1]/div/a/img')
    account_deleted = (By.XPATH, '/html/body/section/div/div/div/h2/b')
    continue_button = (By.ID, 'btn btn-primary')


class Login:

    add_locator = (By.XPATH, '/html/body/ins[2]/div[1]//ins/span/svg/path')
    new_user_signup_locator = (By.XPATH, '/html/body/section/div/div/div[3]/div/h2')
    new_user_name_locator = (By.XPATH, '/html/body/section/div/div/div[3]/div/form/input[2]')
    new_user_email_locator = (By.XPATH, '/html/body/section/div/div/div[3]/div/form/input[3]')
    signup_button_locator = (By.XPATH, '/html/body/section/div/div/div[3]/div/form/button')
    password_locator = (By.ID, 'password')


class Signup:
    enter_account_info_locator = (By.XPATH, '/html/body/section/div/div/div/div/h2/b')
    add_locator = (By.XPATH, '/html/body/div[1]/div/div[2]/svg/path')
    gender_locator = (By.ID, 'id_gender1')
    name_locator = (By.ID, 'name')
    email_locator = (By.ID, 'email')
    password_locator = (By.ID, 'password')
    day_locator = (By.ID, 'days')
    month_locator = (By.ID, 'months')
    year_locator = (By.ID, 'years')
    newsletter_locator = (By.ID, 'newsletter')
    special_offer_locator = (By.ID, 'optin')
    first_name_locator = (By.ID, 'first_name')
    last_name_locator = (By.ID, 'last_name')
    company_locator = (By.ID, 'company')
    address1_locator = (By.ID, 'address1')
    address2_locator = (By.ID, 'address2')
    country_locator = (By.ID, 'country')
    state_locator = (By.ID, 'state')
    city_locator = (By.ID, 'city')
    zipcode_locator = (By.ID, 'zipcode')
    mobile_number_locator = (By.ID, 'mobile_number')
    create_account_button = (By.XPATH, '/html/body/section/div/div/div/div/form/button')


class AccountCreated:
    account_created_locator = (By.XPATH, '/html/body/section/div/div/div/h2/b')
    continue_locator = (By.XPATH,'/html/body/section/div/div/div/div/a')


class DeleteAccount:
    account_deleted_locator = (By.XPATH, '/html/body/section/div/div/div/h2/b')
    continue_button_locator = (By.XPATH, '/html/body/section/div/div/div/div/a')
