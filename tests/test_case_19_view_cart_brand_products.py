from pages.hm_product_page import HMProductPage
from pages.polo_product_page import PoloProductPage
from pages.products_page import ProductsPage
from technical import locators


def test_case_19_view_cart_brand_products(get_main_page):

    main_page = get_main_page

    main_page.click_button(locators.Main.product_button_locator, ProductsPage)

    products_page = main_page.click_button(locators.Main.product_button_locator, ProductsPage)

    products_page.scroll_page_down(300)

    # Verify that Brands are visible on left side bar
    assert products_page.get_text(locators.Products.brands_header_2) == 'Brands'

    hm_products_page = products_page.wait_and_click(locators.Products.HM_brand, 5, HMProductPage)

    # Verify that user is navigated to brand page and brand products are displayed
    assert hm_products_page.get_text(locators.HMProductsPage.summer_top) == 'Summer White Top'

    hm_products_page.scroll_page_down(300)

    polo_products_page = hm_products_page.click_button(locators.HMProductsPage.polo_brand, PoloProductPage)

    # Verify that user is navigated to that brand page and can see products
    assert polo_products_page.get_text(locators.PoloProductsPage.summer_top) == 'Blue Top'