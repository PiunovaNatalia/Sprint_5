from confest import driver
from locators import Locators
from data import Data
from helper import Helper

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestRegister:
    def test_successful_register(self, driver):
        driver.get(Data.REGISTER_URL)

        name_input = driver.find_element(*Locators.REGISTER_NAME_INPUT)
        name_input.send_keys(Data.TEST_NAME)

        email_input = driver.find_element(*Locators.REGISTER_EMAIL_INPUT)
        email_input.send_keys(Helper.generate_email())

        password_input = driver.find_element(*Locators.PASSWORD_INPUT)
        password_input.send_keys(Helper.generate_password())  #Data.TEST_PASSWORD)

        register_button = driver.find_element(*Locators.REGISTER_BUTTON)
        register_button.click()

        WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.LOGIN_PAGE_TITLE))
        login_page_title = driver.find_element(*Locators.LOGIN_PAGE_TITLE)

        assert login_page_title.is_displayed() and login_page_title.text == Data.LOGIN_PAGE_TITLE_TEXT

    def test_incorrect_password(self, driver):
        driver.get(Data.REGISTER_URL)

        name_input = driver.find_element(*Locators.REGISTER_NAME_INPUT)
        name_input.send_keys(Data.TEST_NAME)

        email_input = driver.find_element(*Locators.REGISTER_EMAIL_INPUT)
        email_input.send_keys(Helper.generate_email())

        password_input = driver.find_element(*Locators.PASSWORD_INPUT)
        password_input.send_keys(Data.TEST_INCORRECT_PASSWORD)

        register_button = driver.find_element(*Locators.REGISTER_BUTTON)
        register_button.click()

        WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.INCORRECT_PASSWORD_WARNING))
        incorrect_password_warning_text = driver.find_element(*Locators.INCORRECT_PASSWORD_WARNING)

        assert incorrect_password_warning_text.is_displayed() and incorrect_password_warning_text.text == Data.INCORRECT_PASSWORD_WARNING
