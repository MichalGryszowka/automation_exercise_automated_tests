from pages.test_cases_page import TestCasesPage
from technical import locators


def test_case_7_verify_test_case_page(get_main_page):

    main_page = get_main_page

    # Verify that home page is visible successfully
    assert main_page.check_el_visibility(locators.Main.main_slider_locator) is True

    main_page.click_button(locators.Main.test_case_button, TestCasesPage)

    main_page.switch_to_default_and_refresh()

    test_cases_page = main_page.click_button(locators.Main.test_case_button, TestCasesPage)

    # Verify user is navigated to test cases page successfully
    assert test_cases_page.get_url() == 'https://automationexercise.com/test_cases'