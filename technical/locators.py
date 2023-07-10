from selenium.webdriver.common.by import By


class Main:
    main_slider_locator = (By.ID, "slider")
    login_locator = (By.XPATH, '/html/body/header/div/div/div/div[2]/div/ul/li[4]')
    logged_on_user = (By.XPATH, '/html/body/header/div/div/div/div[2]/div/ul/li[10]/a/b')
    delete_account = (By.XPATH, '/html/body/header/div/div/div/div[2]/div/ul/li[5]/a/i')
    main_page_box = (By.XPATH, '/html/body/header/div/div/div/div[1]/div/a/img')
    account_deleted = (By.XPATH, '/html/body/section/div/div/div/h2/b')
    continue_button = (By.ID, 'btn btn-primary')
    logout_button = (By.XPATH, '/html/body/header/div/div/div/div[2]/div/ul/li[4]/a')
    contact_us_button = (By.XPATH, '/html/body/header/div/div/div/div[2]/div/ul/li[8]/a')
    test_case_button = (By.XPATH, '/html/body/header/div/div/div/div[2]/div/ul/li[5]/a')

class Login:
    existing_email = (By.XPATH, '/html/body/section/div/div/div[1]/div/form/input[2]')
    existing_password = (By.XPATH, '/html/body/section/div/div/div[1]/div/form/input[3]')
    add_locator = (By.XPATH, '/html/body/ins[2]/div[1]//ins/span/svg/path')
    login_to_your_account = (By.XPATH, '/html/body/section/div/div/div[1]/div/h2')
    new_user_signup_locator = (By.XPATH, '/html/body/section/div/div/div[3]/div/h2')
    new_user_name_locator = (By.XPATH, '/html/body/section/div/div/div[3]/div/form/input[2]')
    new_user_email_locator = (By.XPATH, '/html/body/section/div/div/div[3]/div/form/input[3]')
    login_button_locator = (By.XPATH, '/html/body/section/div/div/div[1]/div/form/button')
    signup_button_locator = (By.XPATH, '/html/body/section/div/div/div[3]/div/form/button')
    password_locator = (By.ID, 'password')
    email_incorrect_locator = (By.XPATH, '/html/body/section/div/div/div[1]/div/form/p')
    email_already_exist = (By.XPATH, '/html/body/section/div/div/div[3]/div/form/p')


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


class ContactUs:
    get_in_touch = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/h2')
    name_locator = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[3]/form/div[1]/input')
    email_locator = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[3]/form/div[2]/input')
    subject_locator = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[3]/form/div[3]/input')
    message_locator = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[3]/form/div[4]/textarea')
    upload_file_locator = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[3]/form/div[5]/input')
    submit_locator = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[3]/form/div[6]/input')
    success_message_locator = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]')
    home_button_locator = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[3]/a/span')
    submit_button = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[3]/form/div[6]/input')
    detail_submitted = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]')



