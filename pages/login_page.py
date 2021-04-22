import time

from seleniumbase import BaseCase
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
                self.send_keys(LocatorsLoginPage.PASS_FIELD, x, password)
            with allure.step(LoginPageAllure.CLICK_BUTTON):
                self.click(LocatorsLoginPage.LOGIN_BUTTON)

            error_login = self.wait_for_element('//td[@class="ErrorLabel"]', x, timeout=15)
            print(error_login.text)
            if not error_login:
                self.wait_for_element_present(LocatorsLoginPage.LOGIN_ON_LOGED_PAGE, x, timeout=15 )
                with allure.step(LoginPageAllure.LOGIN_IS_SUCCESS):
                    self.assert_text(login, LocatorsLoginPage.LOGIN_ON_LOGED_PAGE, x, timeout=7)
                return

            if i == 2:
                with allure.step("Go to login error page"):
                    self.wait_for_element_present(LocatorsLoginPage.ERROR_LOGIN_TEXT, x, 15)
                with allure.step("Error page is success open"):
                    assert self.assert_text(self.get_text(LocatorsLoginPage.ERROR_LOGIN_TEXT, x, 15), "ОШИБКА"), \
                        'Login entered three time not correct. Page Error not exists.'
                with allure.step("Support button is present"):
                    assert self.assert_text(
                        self.get_text(LocatorsLoginPage.ERROR_LOGIN_SUPPORT, x), 'службу поддержки.'), \
                        'Support button is not present'
