from pages.base_page import BasePage


class CategoryProducts1Page(BasePage):
    def __init__(self, driver, url='/category_products/1'):
        super().__init__(driver, url)
