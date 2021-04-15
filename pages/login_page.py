from seleniumbase import BaseCase
from locators import LocatorsLoginPage

class LoginPage(BaseCase):

    def login_page(self, url, login, password):
        self.driver.get(url)

        self.wait_for_element_present(LocatorsLoginPage.LOGIN_FIELD, by="By.XPATH", timeout=10)
        self.driver.find_element_by_xpath(LocatorsLoginPage.LOGIN_FIELD).send_keys(login)
        self.driver.find_element_by_xpath(LocatorsLoginPage.PASS_FIELD).send_keys(password)
        self.click(LocatorsLoginPage.LOGIN_BUTTON)
        self.wait_for_element_present(LocatorsLoginPage.LOGIN_ON_LOGED_PAGE, by="By.XPATH", timeout=7)
        self.assert_text(login, LocatorsLoginPage.LOGIN_ON_LOGED_PAGE, by="By.XPATH")