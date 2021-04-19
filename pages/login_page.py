from seleniumbase import BaseCase
from locators import LocatorsLoginPage
from allure_steps import LoginPageAllure
import allure

class LoginPage(BaseCase):

    def login_page(self, url, login, password):
        with allure.step(LoginPageAllure.OPEN_URL):
            self.driver.get(url)
        with allure.step(LoginPageAllure.SEARCH_LOGIN_FIELD):
            self.wait_for_element_present(LocatorsLoginPage.LOGIN_FIELD, by="By.XPATH", timeout=10)
        with allure.step(LoginPageAllure.ENTER_LOGIN):
            self.driver.find_element_by_xpath(LocatorsLoginPage.LOGIN_FIELD).send_keys(login)
        with allure.step(LoginPageAllure.SEARCH_PASS_FIELD):
            self.driver.find_element_by_xpath(LocatorsLoginPage.PASS_FIELD).send_keys(password)
        with allure.step(LoginPageAllure.ENTER_PASS):
            self.click(LocatorsLoginPage.LOGIN_BUTTON)
        with allure.step(LoginPageAllure.SEARCH_BUTTON):
            self.wait_for_element_present(LocatorsLoginPage.LOGIN_ON_LOGED_PAGE, by="By.XPATH", timeout=7)
        with allure.step(LoginPageAllure.CLICK_BUTTON):
            self.assert_text(login, LocatorsLoginPage.LOGIN_ON_LOGED_PAGE, by="By.XPATH")