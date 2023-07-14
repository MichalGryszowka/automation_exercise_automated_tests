from pages.contact_us_page import ContactUsPage
from technical import locators
from technical.user_model import User


def test_case_6_contact_us_form(get_main_page):

    main_page = get_main_page

    # Verify that home page is visible successfully
    assert main_page.check_el_visibility(locators.Main.main_slider_locator) is True

    contact_us_page = main_page.click_button(locators.Main.contact_us_button, ContactUsPage)

    # Verify 'Get In Touch' is visible successfully
    assert contact_us_page.get_text(locators.ContactUs.get_in_touch) == 'Get In Touch'

    contact_us_page.fill_in_data(locators.ContactUs.name_locator, User.name)

    contact_us_page.fill_in_data(locators.ContactUs.email_locator, User.email)

    contact_us_page.fill_in_data(locators.ContactUs.subject_locator, User.subject)

    contact_us_page.fill_in_data(locators.ContactUs.message_locator, User.message)

    contact_us_page.upload_file(locators.ContactUs.upload_file_locator, User.screenshot_path)

    contact_us_page.click_element(locators.ContactUs.submit_button)

    contact_us_page.accept_alert()

    # Verify 'Success! Your details have been submitted successfully.' is visible successfully
    assert contact_us_page.get_text(locators.ContactUs.detail_submitted) == \
           'Success! Your details have been submitted successfully.'