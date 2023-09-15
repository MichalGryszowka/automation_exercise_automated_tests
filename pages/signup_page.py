from pages.base_page import BasePage


class SignupPage(BasePage):
    def __init__(self, driver, url='/signup'):
        super().__init__(driver, url)

