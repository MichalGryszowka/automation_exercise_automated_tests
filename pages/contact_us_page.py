from pages.base_page import BasePage


class ContactUsPage(BasePage):
    def __init__(self, driver, url='/contact_us'):
        super().__init__(driver, url)

