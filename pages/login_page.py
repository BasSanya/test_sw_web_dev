import time

from seleniumbase import BaseCase
from selenium.common.exceptions import NoSuchElementException
from locators import LocatorsLoginPage
from allure_steps import LoginPageAllure
import allure

x = "By.XPATH"

class LoginPage(BaseCase):

    def login_page(self, url, login, password):
        with allure.step(LoginPageAllure.OPEN_URL):
            self.driver.get(url)

        for i in range(3):
            with allure.step(LoginPageAllure.SEARCH_LOGIN_FIELD):
                self.wait_for_element_present(LocatorsLoginPage.LOGIN_FIELD, x, 15)
            with allure.step(LoginPageAllure.ENTER_LOGIN):
                self.clear(LocatorsLoginPage.LOGIN_FIELD, x)
                self.send_keys(LocatorsLoginPage.LOGIN_FIELD, login, x)
            with allure.step(LoginPageAllure.ENTER_PASS):
                self.clear(LocatorsLoginPage.PASS_FIELD, x)
                self.send_keys(LocatorsLoginPage.PASS_FIELD, password, x)
            with allure.step(LoginPageAllure.CLICK_BUTTON):
                self.click(LocatorsLoginPage.LOGIN_BUTTON)
            try:
                self.wait_for_element_present('//td[@class="ErrorLabel"]', x, timeout=10)
            except NoSuchElementException:
                if i == 3:
                    self.wait_for_element_present(LocatorsLoginPage.LOGIN_ON_LOGED_PAGE, x, timeout=15)
                    with allure.step(LoginPageAllure.LOGIN_IS_SUCCESS):
                        self.assert_text(login, LocatorsLoginPage.LOGIN_ON_LOGED_PAGE, x, timeout=7)
                return
