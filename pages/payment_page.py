from pages.base_page import BasePage


class PaymentPage(BasePage):
    def __init__(self, driver, url='/payment'):
        super().__init__(driver, url)
