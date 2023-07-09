from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, url: str):
        self.driver = driver
        self.base_url = 'http://automationexercise.com'
        self.url = url
        self.get()

    def get(self):
        full_url = self.base_url + self.url
        if self.url not in self.driver.current_url:
            self.driver.get(full_url)

    def get_element(self, locator: tuple[By, str]):
        return self.driver.find_element(*locator)

    def fill_in_data(self, locator: tuple[By, str], data: str):
        self.get_element(locator).send_keys(data)

    def get_text(self, locator: tuple[By, str]):
        text = self.driver.find_element(*locator)
        return text.get_attribute('innerHTML')

    def switch_to_default_and_refresh(self):
        self.driver.switch_to.default_content()
        self.driver.refresh()

    def get_url(self):
        return self.driver.current_url

    def click_button(self, locator: tuple[By, str], page):
        self.driver.find_element(*locator).click()
        return page(self.driver, self.driver.current_url)

    def check_el_visibility(self, locator: tuple[By, str]):
        return self.driver.find_element(*locator).is_displayed()

    def select_dropdown(self, locator: tuple[By, str], value: str):
        elem = self.driver.find_element(*locator)
        drop = Select(elem)
        drop.select_by_value(value)

    def upload_file(self, locator: tuple[By, str], path: str):
        self.driver.find_element(*locator).send_keys(path)

    def click_element(self, locator: tuple[By, str]):
        self.driver.find_element(*locator).click()

    def accept_alert(self):
        alert = self.driver.switch_to.alert
        alert.accept()


        #
        #
        # actions = ActionChains(self.driver)
        # self.driver.switch_to.active_element.actions.send_keys(Keys.ENTER)
        # actions.perform()
        #







