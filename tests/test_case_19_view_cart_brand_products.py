from pages.hm_product_page import HMProductPage
from pages.polo_product_page import PoloProductPage
from pages.products_page import ProductsPage
from technical import locators


def test_case_19_view_cart_brand_products(get_main_page):

    main_page = get_main_page

    products_page = main_page.click_button(locators.Main.product_button_locator, ProductsPage)

    products_page.scroll_page_down(300)

    assert products_page.get_text_2(locators.Products.brands_header) == 'BRANDS'

    hm_products_page = products_page.click_button(locators.Products.HM_brand, HMProductPage)

    assert hm_products_page.get_text_2(locators.HMProductsPage.summer_top) == 'Summer White Top'

    hm_products_page.scroll_page_down(600)

    polo_products_page = hm_products_page.click_button(locators.HMProductsPage.polo_brand, PoloProductPage)

    assert polo_products_page.get_text_2(locators.PoloProductsPage.summer_top) == 'Blue Top'