from pages.base_page import BasePage


class HMProductPage(BasePage):
    def __init__(self, driver, url='/brand_products/H&M'):
        super().__init__(driver, url)

