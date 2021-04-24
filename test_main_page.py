from pages.main_page import MainPage
import pytest
import allure


@allure.story("Test Main Page")
class TestMainPage(MainPage):
    login_parametrs = [{
        'url': 'https://appunilever.datacenter.ssbs.com.ua/SalesWorksWeb/Login.aspx?ReturnUrl=%2fSalesWorksWeb%2fdefault.aspx',
        'login': 'bbuhe',
        'password': '%YvdvIjV28'}
    ]

    @allure.suite("Sales Works main tests")
    @allure.title("Test side menu of main page")
    def test_side_menu_blocks(self):
        self.login_page(**self.login_parametrs[0])

        self.check_1L_catalogs_are_present()

        self.open_help_menu()

        self.open_users_dir()

        self.open_other_dir()

        # Перевірити відкриття кожного довідника
        # Перевірка генерації звітів
        # test1
