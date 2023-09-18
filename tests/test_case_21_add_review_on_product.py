from pages.product_details_1_page import ProductsDetails1Page
from pages.products_page import ProductsPage
from technical import locators
from technical.user_model import User


def test_case_21_add_review_on_product(get_main_page):

    main_page = get_main_page

    products_page = main_page.click_button(locators.Main.product_button_locator, ProductsPage)

    # Verify user is navigated to ALL PRODUCTS page successfully
    assert products_page.get_url() == 'https://automationexercise.com/products'

    products_page.scroll_page_down(300)

    products_details_1 = products_page.click_button(locators.Products.view_product_blue_top, ProductsDetails1Page)

    # Verify 'Write Your Review' is visible
    assert products_details_1.check_el_visibility(locators.ProductsDetail1.write_your_review) is True

    products_details_1.fill_in_data(locators.ProductsDetail1.your_name, User.name)

    products_details_1.fill_in_data(locators.ProductsDetail1.email, User.email)

    products_details_1.fill_in_data(locators.ProductsDetail1.review, User.review)

    products_details_1.click_element(locators.ProductsDetail1.submit)

    # Verify success message 'Thank you for your review.'
    assert products_details_1.get_text(locators.ProductsDetail1.thank_you_msg) == 'Thank you for your review.'








