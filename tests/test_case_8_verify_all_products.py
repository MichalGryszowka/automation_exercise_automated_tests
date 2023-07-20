from pages.product_details_1_page import ProductsDetails1Page
from pages.products_page import ProductsPage
from technical import locators


def test_case_8_verify_all_products(get_main_page):

    main_page = get_main_page

    # Verify that home page is visible successfully
    assert main_page.check_el_visibility(locators.Main.main_slider_locator) is True

    main_page.click_button(locators.Main.product_button_locator, ProductsPage)

    main_page.switch_to_default_and_refresh()

    products_page = main_page.click_button(locators.Main.product_button_locator, ProductsPage)

    # Verify user is navigated to ALL PRODUCTS page successfully
    assert products_page.get_url() == 'https://automationexercise.com/products'

    # Verify the products list is visible
    assert products_page.check_el_visibility(locators.Products.product_list_locator) is True

    product_details_1_page = products_page.click_button(locators.Products.product_details_1_view_locator,
                                                        ProductsDetails1Page)

    # Verify that product name is visible
    assert product_details_1_page.get_text(locators.Products.product_details_1_name_locator) == 'Blue Top'

    # Verify that category is visible
    assert product_details_1_page.get_text_2(
        locators.Products.product_details_1_category_locator) == 'Category: Women > Tops'

    # Verify that price is visible
    assert product_details_1_page.get_text_2(
        locators.Products.product_details_1_price_locator) == 'Rs. 500'

    # Verify that availability is visible
    assert product_details_1_page.get_text_2(
        locators.Products.product_details_1_availab_locator) == 'Availability: In Stock'

    # Verify that condition is visible
    assert product_details_1_page.get_text_2(
        locators.Products.product_details_1_condition_locator) == 'Condition: New'

    # Verify that brand is visible
    assert product_details_1_page.get_text_2(
        locators.Products.product_details_1_brand_locator) == 'Brand: Polo'








