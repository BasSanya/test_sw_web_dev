from pages.main_page import MainPage
import pytest
import allure


class TestMainPage(MainPage):
    url = 'https://appunilevertest.datacenter.ssbs.com.ua/SalesWorksWeb/Login.aspx?ReturnUrl=%2fSalesWorksWeb%2fdefault.aspx'
    login = 'olekb01'
    password = '%x8&Eh5-F8_SrPa5'


    @allure.title("Test Main Page")
    def test_side_menu_blocks(self):

        self.login_page(self.url, self.login, self.password)

        self.check_1L_catalogs_are_present()

        self.open_help_menu()

        #Перевірити відкриття кожного довідника
        #Перевірка генерації звітів
        #test1