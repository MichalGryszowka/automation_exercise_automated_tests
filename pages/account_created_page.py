from pages.base_page import BasePage


class AccountCreatedPage(BasePage):
    def __init__(self, driver, url='/account_created.html'):
        super().__init__(driver, url)