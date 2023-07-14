from pages.base_page import BasePage


class ProductsDetails1Page(BasePage):
    def __init__(self, driver, url='product_details/1'):
        super().__init__(driver, url)

