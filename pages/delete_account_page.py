from pages.base_page import BasePage


class DeleteAccountPage(BasePage):
    def __init__(self, driver, url='/delete_account'):
        super().__init__(driver, url)
