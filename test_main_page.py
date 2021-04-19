from pages.main_page import MainPage
import pytest
import allure

class TestMainPage(MainPage):
    url = 'https://appunileverdev.datacenter.ssbs.com.ua/SalesWorksWeb/Login.aspx?ReturnUrl=%2fSalesWorksWeb%2fdefault.aspx'
    login = 'bbuhe'
    password = '%YvdvIjV28'

    @allure.title("Test Main Page")
    def test_side_menu_blocks(self):

        self.login_page(self.url, self.login, self.password)

        self.check_all_catalogs_are_present()