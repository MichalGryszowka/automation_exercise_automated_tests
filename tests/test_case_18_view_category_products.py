from pages.category_products_1_page import CategoryProducts1Page
from pages.category_products_3_page import CategoryProducts3Page
from pages.main_page import MainPage
from technical import locators


def test_case_18_view_category_products(get_main_page):

    main_page = get_main_page

    # Verify that home page is visible successfully
    assert main_page.check_el_visibility(locators.Main.category_products) is True

    main_page.click_button(locators.Main.woman_category, MainPage)

    cat_prod_1_page = main_page.wait_and_click(locators.Main.woman_category_dress, 2, CategoryProducts1Page)

    assert cat_prod_1_page.get_text(locators.CategoryProducts1.dress_products_title) == 'Women - Dress Products'

    cat_prod_1_page.scroll_page_down(400)

    cat_prod_1_page.click_element(locators.CategoryProducts1.man_category)

    cat_prod_1_page.wait_and_click(locators.CategoryProducts1.man_category_tshirts, 2, CategoryProducts3Page)

    cat_prod_1_page.switch_to_default_and_refresh()

    cat_prod_1_page.click_element(locators.CategoryProducts1.man_category)

    cat_prod_3_page = cat_prod_1_page.wait_and_click(
        locators.CategoryProducts1.man_category_tshirts, 2, CategoryProducts3Page)

    assert cat_prod_3_page.get_text(locators.CategoryProducts3.tshirts_products_title) ==\
           'Men - Tshirts Products'
