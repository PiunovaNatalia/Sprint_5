from confest import driver, driver_logged
from locators import Locators
from data import Data

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestPersonalAccount:
    def test_open_account_page(self, driver_logged):
        personal_account_button = driver_logged.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON)
        personal_account_button.click()

        WebDriverWait(driver_logged, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.PROFILE_LINK))
        profile_link_text = driver_logged.find_element(*Locators.PROFILE_LINK)

        assert profile_link_text.is_displayed() and profile_link_text.text == Data.PROFILE_LINK_TEXT
