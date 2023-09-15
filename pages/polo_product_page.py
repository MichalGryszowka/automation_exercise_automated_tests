from pages.base_page import BasePage


class PoloProductPage(BasePage):
    def __init__(self, driver, url='/brand_products/Polo'):
        super().__init__(driver, url)

