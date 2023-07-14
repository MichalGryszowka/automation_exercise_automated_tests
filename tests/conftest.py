from pytest import fixture
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.main_page import MainPage


@fixture
def init_driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.set_window_size(1020, 1200)
    yield driver
    driver.close()


@fixture
def get_main_page(init_driver):
    return MainPage(init_driver)
