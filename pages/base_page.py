from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import os.path
import time

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

    def get_text_2(self, locator: tuple[By, str]):
        text = self.driver.find_element(*locator)
        return text.get_attribute('innerText')

    def switch_to_default_and_refresh(self):
        self.driver.switch_to.default_content()
        self.driver.refresh()

    def get_url(self):
        self.driver.refresh()
        return str(self.driver.current_url)

    def click_button(self, locator: tuple[By, str], page):
        self.driver.find_element(*locator).click()
        if "google_vignette" in self.driver.current_url:
            self.driver.refresh()
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()
        return page(self.driver, self.driver.current_url)

    def wait_and_get_text(self, locator: tuple[By, str], time: int):
        element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(
            locator))
        element.get_text(locator)

    def wait_and_get_text_2(self, locator: tuple[By, str], time: int):
        element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(
            locator))
        element.get_text_2(locator)

    def check_el_visibility(self, locator: tuple[By, str]):
        return self.driver.find_element(*locator).is_displayed()

    def select_dropdown(self, locator: tuple[By, str], value: str):
        elem = self.driver.find_element(*locator)
        drop = Select(elem)
        drop.select_by_value(value)

    def upload_file(self, locator: tuple[By, str], path: str):
        self.driver.find_element(*locator).send_keys(path)

    def click_element(self, locator: tuple[By, str]):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()

    def accept_alert(self):
        alert = self.driver.switch_to.alert
        alert.accept()

    def scroll_page_down(self, pixels: int):
        self.driver.execute_script(f"window.scrollBy(0,{pixels})", "")

    def hover_cursor(self, locator: tuple[By, str]):
        action = ActionChains(self.driver)
        el = self.driver.find_element(*locator)
        action.move_to_element(el).perform()

    def wait_and_click(self, locator: tuple[By, str], time: int, page):
        element = WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(
            locator))
        element.click()
        return page(self.driver, self.driver.current_url)

    def return_page(self):
        self.driver.back()

    def check_file_download(self, path: str):
        while not os.path.exists(path):
            time.sleep(1)
        if os.path.isfile(path):
            return True





















