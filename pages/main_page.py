from locators import LocatorsMainPage
from .login_page import LoginPage


class MainPage(LoginPage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def check_all_catalogs_are_present(self):
        self.is_element_present(LocatorsMainPage.MP_USERS, by="By.XPATH")
        self.is_element_present(LocatorsMainPage.MP_OTHER_CATALOG, by="By.XPATH")
        self.is_element_present(LocatorsMainPage.MP_SALES_STUCTURES, by="By.XPATH")
        self.is_element_present(LocatorsMainPage.MP_OUTLETS, by="By.XPATH")
        self.is_element_present(LocatorsMainPage.MP_PRODUCTS, by="By.XPATH")
        self.is_element_present(LocatorsMainPage.MP_DOCUMENTS, by="By.XPATH")
        self.is_element_present(LocatorsMainPage.MP_PLAN_AND_ANALIS, by="By.XPATH")
        self.is_element_present(LocatorsMainPage.MP_REPORTS, by="By.XPATH")
        self.is_element_present(LocatorsMainPage.MP_DATA_TRANSFER, by="By.XPATH")