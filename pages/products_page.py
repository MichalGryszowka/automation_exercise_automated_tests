from pages.base_page import BasePage


class ProductsPage(BasePage):
    def __init__(self, driver, url='/products'):
        super().__init__(driver, url)

