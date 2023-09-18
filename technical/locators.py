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
    view_first_product = (By.XPATH, '/html/body/section[2]/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/ul/li/a')
    category_products = (By.XPATH, '/html/body/section[2]/div/div/div[1]/div/h2')
    woman_category = (By.CSS_SELECTOR, '#accordian > div:nth-child(1) > div.panel-heading > h4 > a > span > i')
    woman_category_dress = (By.CSS_SELECTOR, '#Women > div > ul > li:nth-child(1) > a')
    dress_products_title = (By.XPATH, '/html/body/section/div/div[2]/div[2]/div/h2')
    man_category = (By.CSS_SELECTOR , '#accordian > div:nth-child(2) > div.panel-heading > h4 > a > span > i')
    tshirts_products_title = (By.CSS_SELECTOR,
                              'body > section > div > div.row > div.col-sm-9.padding-right > div > div:nth-child(3) > div > div.single-products > div.product-overlay > div > p')
    recommended_items = (By.CSS_SELECTOR, 'body > section:nth-child(3) > div > div > div.col-sm-9.padding-right > div.recommended_items > h2')
    add_to_cart_stylish_dress = (By. CSS_SELECTOR, '#recommended-item-carousel > div > div.item.active > div:nth-child(1) > div > div > div > a')
    view_cart_blue_top = (By. CSS_SELECTOR, '#cartModal > div > div > div.modal-body > p:nth-child(2) > a > u')



class Login:
    existing_email = (By.XPATH, '/html/body/section/div/div/div[1]/div/form/input[2]')
    existing_password = (By.XPATH, '/html/body/section/div/div/div[1]/div/form/input[3]')
    add_locator = (By.XPATH, '/html/body/ins[2]/div[1]//ins/span/svg/path')
    login_to_your_account = (By.XPATH, '//*[@id="form"]/div/div/div[1]/div/h2')
    new_user_signup_locator = (By.XPATH, '/html/body/section/div/div/div[3]/div/h2')
    new_user_name_locator = (By.XPATH, '/html/body/section/div/div/div[3]/div/form/input[2]')
    new_user_email_locator = (By.XPATH, '/html/body/section/div/div/div[3]/div/form/input[3]')
    login_button_locator = (By.XPATH, '/html/body/section/div/div/div[1]/div/form/button')
    signup_button_locator = (By.XPATH, '/html/body/section/div/div/div[3]/div/form/button')
    password_locator = (By.ID, 'password')
    email_incorrect_locator = (By.XPATH, '/html/body/section/div/div/div[1]/div/form/p')
    email_already_exist = (By.XPATH, '/html/body/section/div/div/div[3]/div/form/p')


class Signup:
    enter_account_info_locator = (By.CSS_SELECTOR, '#form > div > div > div > div.login-form > h2 > b')
    add_locator = (By.XPATH, '/html/body/div[1]/div/div[2]/svg/path')
    gender_locator = (By.CSS_SELECTOR, '#id_gender1')
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
    brands_header = (By.CSS_SELECTOR, 'body > section:nth-child(4) > div.container > div > div.col-sm-3 > div.left-sidebar > div.brands_products > h2')
    brands_header_2 = (By.CSS_SELECTOR, 'body > section:nth-child(3) > div.container > div > div.col-sm-3 > div.left-sidebar > div.brands_products > h2')
    HM_brand = (By.CSS_SELECTOR, 'body > section:nth-child(3) > div.container > div > div.col-sm-3 > div.left-sidebar > div.brands_products > div > ul > li:nth-child(2) > a')
    summer_top = (By.CSS_SELECTOR,
                  'body > section > div > div.row > div.col-sm-9.padding-right > div > div:nth-child(4) > div > div.single-products > div.product-overlay > div > p')
    view_product_blue_top = (By.CSS_SELECTOR, 'body > section:nth-child(3) > div.container > div > div.col-sm-9.padding-right > div > div:nth-child(3) > div > div.choose > ul > li > a')


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
    proceed_to_checkout_btn = (By.XPATH, '//*[@id="do_action"]/div[1]/div/div/a')
    register_login_button = (By.XPATH, '//*[@id="checkoutModal"]/div/div/div[2]/p[2]/a/u')
    signup_login = (By.CSS_SELECTOR, '#header > div > div > div > div.col-sm-8 > div > ul > li:nth-child(4) > a')
    cart_is_empty_msg = (By.CSS_SELECTOR, '#empty_cart > p > b')
    view_stylish_dress_in_basket = (By.CSS_SELECTOR, '#product-4 > td.cart_description > h4 > a')


class Checkout:
    address_details = (By.XPATH, '//*[@id="cart_items"]/div/div[2]/h2')
    review_your_order = (By.XPATH, '//*[@id="cart_items"]/div/div[4]/h2')
    place_order_btn = (By.XPATH, '//*[@id="cart_items"]/div/div[7]/a')
    comment_box = (By.XPATH, '//*[@id="ordermsg"]/textarea')
    delete_account = (By.CSS_SELECTOR, '#header > div > div > div > div.col-sm-8 > div > ul > li:nth-child(5) > a')


class Payment:
    name_on_card = (By.XPATH, '//*[@id="payment-form"]/div[1]/div/input')
    card_number = (By.CSS_SELECTOR, '#payment-form > div:nth-child(3) > div > input')
    cvc = (By.XPATH, '//*[@id="payment-form"]/div[3]/div[1]/input')
    expiration_month = (By.XPATH, '//*[@id="payment-form"]/div[3]/div[2]/input')
    expiration_year = (By.XPATH, '//*[@id="payment-form"]/div[3]/div[3]/input')
    pay_and_confirm_btn = (By.XPATH, '//*[@id="submit"]')
    your_order_placed = (By.XPATH, '//*[@id="success_message"]/div')


class PaymentDone:
    delete_my_account = (By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[5]/a')


class CategoryProducts1:
    dress_products_title = (By.XPATH, '/html/body/section/div/div[2]/div[2]/div/h2')
    man_category = (By.CSS_SELECTOR , '#accordian > div:nth-child(2) > div.panel-heading > h4 > a > span > i')
    man_category_tshirts = (By.CSS_SELECTOR, '#Men > div > ul > li:nth-child(1) > a')
    category_products = (By.XPATH, '/html/body/section[2]/div/div/div[1]/div/h2')
    woman_category_dress = (By.CSS_SELECTOR, '#Women > div > ul > li:nth-child(1) > a')


class CategoryProducts3:
    tshirts_products_title = (By.CSS_SELECTOR, 'body > section > div > div.row > div.col-sm-9.padding-right > div > div:nth-child(3) > div > div.single-products > div.product-overlay > div > p')


class HMProductsPage:
    summer_top = (By.CSS_SELECTOR, 'body > section > div > div.row > div.col-sm-9.padding-right > div > div:nth-child(4) > div > div.single-products > div.product-overlay > div > p')
    polo_brand = (By.CSS_SELECTOR, 'body > section > div > div.row > div.col-sm-3 > div > div.brands_products > div > ul > li:nth-child(1) > a')


class PoloProductsPage:
    summer_top = (By.CSS_SELECTOR,'body > section > div > div.row > div.col-sm-9.padding-right > div > div:nth-child(3) > div > div.single-products > div.product-overlay > div > p')


class ProductsDetail1:
    write_your_review = (By.CSS_SELECTOR, 'body > section > div > div > div.col-sm-9.padding-right > div.category-tab.shop-details-tab > div.col-sm-12 > ul > li > a')
    your_name = (By. CSS_SELECTOR, '#name')
    email = (By. CSS_SELECTOR, '#email')
    review = (By.CSS_SELECTOR, '#review')
    submit = (By. ID, 'button-review')
    thank_you_msg = (By. CSS_SELECTOR, '#review-section > div > div > span')