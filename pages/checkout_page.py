from pages.base_page import BasePage


class CheckoutPage(BasePage):
    def __init__(self, driver, url='/checkout'):
        super().__init__(driver, url)
