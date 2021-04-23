import time

from seleniumbase import BaseCase
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from locators import LocatorsLoginPage
from allure_steps import LoginPageAllure
import allure

class LoginPage(BaseCase):

    def login_page(self, url, login, password):
        with allure.step(LoginPageAllure.OPEN_URL):
            self.driver.get(url)

        for i in range(3):
            with allure.step(LoginPageAllure.SEARCH_LOGIN_FIELD):
                self.wait_for_element_present(LocatorsLoginPage.LOGIN_FIELD, by=By.XPATH, timeout=15)
            with allure.step(LoginPageAllure.ENTER_LOGIN):
                self.clear(LocatorsLoginPage.LOGIN_FIELD, by=By.XPATH)
                self.send_keys(LocatorsLoginPage.LOGIN_FIELD, login, by=By.XPATH)
            with allure.step(LoginPageAllure.ENTER_PASS):
                self.clear(LocatorsLoginPage.PASS_FIELD, by=By.XPATH)
                self.send_keys(LocatorsLoginPage.PASS_FIELD, password, by=By.XPATH)
            with allure.step(LoginPageAllure.CLICK_BUTTON):
                self.click(LocatorsLoginPage.LOGIN_BUTTON)
            # with
            try:
                self.wait_for_element_present(LocatorsLoginPage.ERROR_ENTERED_MESSAGE, by=By.XPATH, timeout=10)
            except NoSuchElementException:
                self.wait_for_element_present(LocatorsLoginPage.LOGIN_ON_LOGGED_PAGE, by=By.XPATH, timeout=15)
                with allure.step(LoginPageAllure.LOGIN_IS_SUCCESS):
                    self.assert_text(login, LocatorsLoginPage.LOGIN_ON_LOGGED_PAGE, by=By.XPATH, timeout=7)
                return
