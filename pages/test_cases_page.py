from pages.base_page import BasePage


class TestCasesPage(BasePage):
    def __init__(self, driver, url='/test_cases.html'):
        super().__init__(driver, url)
