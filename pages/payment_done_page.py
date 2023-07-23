from pages.base_page import BasePage


class PaymentDonePage(BasePage):
    def __init__(self, driver, url='/payment_done/0'):
        super().__init__(driver, url)
