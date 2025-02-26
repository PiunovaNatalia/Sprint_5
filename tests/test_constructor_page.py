from confest import driver, driver_logged
from locators import Locators
from data import Data

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestConstructor:
    def test_open_constructor(self, driver_logged):
        login_button = driver_logged.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON)
        login_button.click()

        WebDriverWait(driver_logged, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.CONSTRUCTOR_LINK))

        constructor_button = driver_logged.find_element(*Locators.CONSTRUCTOR_LINK)
        constructor_button.click()

        WebDriverWait(driver_logged, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.CONSTRUCTOR_TITLE))
        constructor_title_text = driver_logged.find_element(*Locators.CONSTRUCTOR_TITLE)

        assert constructor_title_text.is_displayed() and constructor_title_text.text == Data.CONSTRUCTOR_TITLE_TEXT

    def test_open_constructor_via_logo(self, driver_logged):
        login_button = driver_logged.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON)
        login_button.click()

        WebDriverWait(driver_logged, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.CONSTRUCTOR_LINK))

        constructor_button = driver_logged.find_element(*Locators.LOGOTYPE)
        constructor_button.click()

        WebDriverWait(driver_logged, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.CONSTRUCTOR_TITLE))
        constructor_title_text = driver_logged.find_element(*Locators.CONSTRUCTOR_TITLE)

        assert constructor_title_text.is_displayed() and constructor_title_text.text == Data.CONSTRUCTOR_TITLE_TEXT

    def test_open_sauces_tab(self, driver_logged):
        WebDriverWait(driver_logged, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.SAUCES_TAB_BUTTON))
        constructor_button = driver_logged.find_element(*Locators.SAUCES_TAB_BUTTON)
        constructor_button.click()

        WebDriverWait(driver_logged, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.SELECTED_SAUCES_TAB))
        selected_tab = driver_logged.find_element(*Locators.SELECTED_SAUCES_TAB)

        assert selected_tab.is_displayed() and selected_tab.text == Data.SAUCES_TAB_TEXT

    def test_open_filling_tab(self, driver_logged):
        WebDriverWait(driver_logged, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.FILLING_TAB_BUTTON))
        constructor_button = driver_logged.find_element(*Locators.FILLING_TAB_BUTTON)
        constructor_button.click()

        WebDriverWait(driver_logged, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.SELECTED_FILLING_TAB))
        selected_tab = driver_logged.find_element(*Locators.SELECTED_FILLING_TAB)

        assert selected_tab.is_displayed() and selected_tab.text == Data.FILLING_TAB_TEXT

    def test_open_bread_tab_after_open_sauces_tab(self, driver_logged):
        WebDriverWait(driver_logged, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.SAUCES_TAB_BUTTON))
        constructor_button = driver_logged.find_element(*Locators.SAUCES_TAB_BUTTON)
        constructor_button.click()

        WebDriverWait(driver_logged, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.SELECTED_SAUCES_TAB))

        constructor_button = driver_logged.find_element(*Locators.BREAD_TAB_BUTTON)
        constructor_button.click()

        WebDriverWait(driver_logged, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.SELECTED_BREAD_TAB))
        selected_tab = driver_logged.find_element(*Locators.SELECTED_BREAD_TAB)

        WebDriverWait(driver_logged, 60)

        assert selected_tab.is_displayed() and selected_tab.text == Data.BREAD_TAB_TEXT