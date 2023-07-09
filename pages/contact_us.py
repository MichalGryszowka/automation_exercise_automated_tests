from pages.base_page import BasePage


class ContactUsPage(BasePage):
    def __init__(self, driver, url='/contact_us.html'):
        super().__init__(driver, url)

