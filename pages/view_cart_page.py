from pages.base_page import BasePage


class ViewCartPage(BasePage):
    def __init__(self, driver, url='/view_cart'):
        super().__init__(driver, url)
