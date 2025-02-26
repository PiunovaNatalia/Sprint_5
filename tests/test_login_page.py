from confest import driver, driver_main_page
from locators import Locators
from data import Data

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLogin:
    def test_login_via_login_in_account_button(self, driver_main_page):
        login_button = driver_main_page.find_element(*Locators.LOGIN_IN_ACCOUNT_BUTTON)
        login_button.click()

        WebDriverWait(driver_main_page, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.LOGIN_PAGE_TITLE))

        email_input = driver_main_page.find_element(*Locators.EMAIL_INPUT)
        email_input.send_keys(Data.TEST_EMAIL)

        password_input = driver_main_page.find_element(*Locators.PASSWORD_INPUT)
        password_input.send_keys(Data.TEST_PASSWORD)

        login_button = driver_main_page.find_element(*Locators.LOGIN_BUTTON)
        login_button.click()

        WebDriverWait(driver_main_page, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.SECTION_TITLE))

        section_title = driver_main_page.find_element(*Locators.SECTION_TITLE)

        assert section_title.is_displayed() and section_title.text == Data.SECTION_TITLE_TEXT


    def test_login_via_personal_account_button(self, driver_main_page):
        login_button = driver_main_page.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON)
        login_button.click()

        WebDriverWait(driver_main_page, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.LOGIN_PAGE_TITLE))

        email_input = driver_main_page.find_element(*Locators.EMAIL_INPUT)
        email_input.send_keys(Data.TEST_EMAIL)

        password_input = driver_main_page.find_element(*Locators.PASSWORD_INPUT)
        password_input.send_keys(Data.TEST_PASSWORD)

        login_button = driver_main_page.find_element(*Locators.LOGIN_BUTTON)
        login_button.click()

        WebDriverWait(driver_main_page, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.SECTION_TITLE))

        section_title = driver_main_page.find_element(*Locators.SECTION_TITLE)

        assert section_title.is_displayed() and section_title.text == Data.SECTION_TITLE_TEXT

    def test_login_via_register_page(self, driver):
        driver.get(Data.REGISTER_URL)
        login_button = driver.find_element(*Locators.LOGIN_THROUGH_REGISTER_PAGE_LINK)
        login_button.click()

        WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.LOGIN_PAGE_TITLE))

        email_input = driver.find_element(*Locators.EMAIL_INPUT)
        email_input.send_keys(Data.TEST_EMAIL)

        password_input = driver.find_element(*Locators.PASSWORD_INPUT)
        password_input.send_keys(Data.TEST_PASSWORD)

        login_button = driver.find_element(*Locators.LOGIN_BUTTON)
        login_button.click()

        WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.SECTION_TITLE))

        section_title = driver.find_element(*Locators.SECTION_TITLE)

        assert section_title.is_displayed() and section_title.text == Data.SECTION_TITLE_TEXT

    def test_login_via_forgot_password_page(self, driver):
        driver.get(Data.FORGOT_PASSWORD_URL)
        login_button = driver.find_element(*Locators.LOGIN_THROUGH_REGISTER_PAGE_LINK)
        login_button.click()

        WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.LOGIN_PAGE_TITLE))

        email_input = driver.find_element(*Locators.EMAIL_INPUT)
        email_input.send_keys(Data.TEST_EMAIL)

        password_input = driver.find_element(*Locators.PASSWORD_INPUT)
        password_input.send_keys(Data.TEST_PASSWORD)

        login_button = driver.find_element(*Locators.LOGIN_BUTTON)
        login_button.click()

        WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.SECTION_TITLE))

        section_title = driver.find_element(*Locators.SECTION_TITLE)

        assert section_title.is_displayed() and section_title.text == Data.SECTION_TITLE_TEXT