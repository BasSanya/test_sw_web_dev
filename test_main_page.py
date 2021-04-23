from pages.main_page import MainPage
import pytest
import allure


class TestMainPage(MainPage):
    login_parametrs = [{
        'url': 'https://appunileverdev.datacenter.ssbs.com.ua/SalesWorksWeb/Login.aspx?ReturnUrl=%2fSalesWorksWeb%2fdefault.aspx',
        'login': 'bbuhe',
        'password': '%YvdvIjV28'}
    ]

    @allure.title("Test Main Page")
    def test_side_menu_blocks(self):
        self.login_page(**self.login_parametrs[0])

        self.check_1L_catalogs_are_present()

        self.open_help_menu()

        # Перевірити відкриття кожного довідника
        # Перевірка генерації звітів
        # test1
