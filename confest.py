from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pytest
from data import Data
from locators import Locators


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    yield driver

    driver.quit()

@pytest.fixture(scope="function")
def driver_main_page(driver):
    driver.get(Data.MAIN_PAGE_URL)

    yield driver

@pytest.fixture(scope="function")
def driver_logged(driver):
    driver.get(Data.LOGIN_URL)
    email_input = driver.find_element(*Locators.EMAIL_INPUT)
    email_input.send_keys(Data.TEST_EMAIL)

    password_input = driver.find_element(*Locators.PASSWORD_INPUT)
    password_input.send_keys(Data.TEST_PASSWORD)

    login_button = driver.find_element(*Locators.LOGIN_BUTTON)
    login_button.click()

    yield driver
