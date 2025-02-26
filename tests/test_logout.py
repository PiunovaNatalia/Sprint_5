from confest import driver, driver_logged
from locators import Locators
from data import Data

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLogout:
    def test_logout(self, driver_logged):
        personal_account_button = driver_logged.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON)
        personal_account_button.click()
        WebDriverWait(driver_logged, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.LOGOUT_BUTTON))

        logout_button = driver_logged.find_element(*Locators.LOGOUT_BUTTON)
        logout_button.click()
        WebDriverWait(driver_logged, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.LOGIN_PAGE_TITLE))

        login_page_title = driver_logged.find_element(*Locators.LOGIN_PAGE_TITLE)

        assert login_page_title.is_displayed() and login_page_title.text == Data.LOGIN_PAGE_TITLE_TEXT
