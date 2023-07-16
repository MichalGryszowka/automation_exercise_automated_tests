from pages.base_page import BasePage


class ViewCart(BasePage):
    def __init__(self, driver, url='/view_cart.html'):
        super().__init__(driver, url)
