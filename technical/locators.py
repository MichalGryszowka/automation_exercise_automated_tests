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
    subscription_locator = (By.CSS_SELECTOR, 'div.single-widget > h2')
    subscription_mail_locator = (By.ID, 'susbscribe_email')
    subscription_button_locator = (By.XPATH, '//*[@id="subscribe"]/i')
    subscription_success_msg = (By.XPATH, '//*[@id="success-subscribe"]/div')
    cart_button_locator = (By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[3]/a')
    product_button_locator = (By.XPATH, '/html/body/header/div/div/div/div[2]/div/ul/li[2]/a')
    view_first_product = (By.XPATH, '/html/body/section[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div/div[2]/ul/li/a')


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
    continue_locator = (By.XPATH, '/html/body/section/div/div/div/div/a')


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


class Products:
    product_list_locator = (By.CLASS_NAME, 'brands-name')
    product_details_1_view_locator = (By.XPATH, '/html/body/section[2]/div/div/div[2]/div/div[2]/div/div[2]/ul/li/a')
    product_details_1_name_locator = (By.XPATH, '/html/body/section/div/div/div[2]/div[2]/div[2]/div/h2')
    product_details_1_category_locator = (By.XPATH, '/html/body/section/div/div/div[2]/div[2]/div[2]/div/p[1]')
    product_details_1_price_locator = (By.XPATH, '/html/body/section/div/div/div[2]/div[2]/div[2]/div/span/span')
    product_details_1_availab_locator = (By.XPATH, '/html/body/section/div/div/div[2]/div[2]/div[2]/div/p[2]')
    product_details_1_condition_locator = (By.XPATH, '/html/body/section/div/div/div[2]/div[2]/div[2]/div/p[3]')
    product_details_1_brand_locator = (By.XPATH, '/html/body/section/div/div/div[2]/div[2]/div[2]/div/p[4]')
    search_product_locator = (By.ID, 'search_product')
    loop_locator = (By.XPATH, '/html/body/section[1]/div/button/i')
    searched_products_locator = (By.XPATH, '/html/body/section[2]/div/div/div[2]/div/h2')
    searched_blue_top = (By.XPATH, '/html/body/section[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/p')
    hover_first_product_locator = (By.XPATH, '/html/body/section[2]/div[1]/div/div[2]/div/div[2]/div/div[1]')
    add_to_cart_first_product = (By.XPATH, '/html/body/section[2]/div[1]/div/div[2]/div/div[2]/div/div[1]/div[2]/div/a')
    continue_shopping_button_locator = (By.CSS_SELECTOR, "#cartModal > div > div > div.modal-footer > button")
    hover_second_product_locator = (By.XPATH, '/html/body/section[2]/div/div/div[2]/div/div[3]/div/div[1]/div[1]')
    add_to_cart_second_product = (By.XPATH, '/html/body/section[2]/div/div/div[2]/div/div[3]/div/div[1]/div[2]/div/a')
    view_cart_locator = (By. CSS_SELECTOR, '#cartModal > div > div > div.modal-body > p:nth-child(2) > a > u')
    unit_price_first_product = (By.XPATH, '//*[@id="product-1"]/td[3]/p')
    qty_first_product = (By.XPATH, '//*[@id="product-1"]/td[4]/button')
    total_price_first_product = (By.XPATH, '//*[@id="product-1"]/td[5]/p')
    unit_price_second_product = (By.XPATH, '//*[@id="product-2"]/td[3]/p')
    qty_second_product = (By.XPATH, '//*[@id="product-2"]/td[4]/button')
    total_price_second_product = (By.XPATH, '//*[@id="product-2"]/td[5]/p')
    dynamic_qty_first_product = (By.XPATH, '//*[@id="quantity"]')
    to_cart_first_product = (By.XPATH, '/html/body/section/div/div/div[2]/div[2]/div[2]/div/span/button')


class ViewCart:
    subscription_locator = (By.CSS_SELECTOR, 'div.single-widget > h2')
    subscription_mail_locator = (By.ID, 'susbscribe_email')
    subscription_button_locator = (By.XPATH, '//*[@id="subscribe"]')
    subscription_success_msg = (By.XPATH, '//*[@id="success-subscribe"]/div')
    first_product_in_cart_locator = (By.XPATH, '//*[@id="product-1"]/td[2]/h4/a')
    second_product_in_cart_locator = (By.XPATH, '//*[@id="product-2"]/td[2]/h4/a')
    first_product_in_cart_basket = (By.XPATH, '//*[@id="product-1"]/td[2]/h4/a')
    second_product_in_cart_basket = (By.XPATH, '//*[@id="product-2"]/td[2]/h4/a')
    delete_x_button_first_product = (By.XPATH, '//*[@id="product-1"]/td[6]/a')
    delete_x_button_second_product = (By.XPATH, '//*[@id="product-2"]/td[6]/a/i')



