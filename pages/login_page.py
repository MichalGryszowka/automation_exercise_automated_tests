from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver, url='/login'):
        super().__init__(driver, url)