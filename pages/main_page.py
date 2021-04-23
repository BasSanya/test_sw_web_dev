from selenium.webdriver.common.keys import Keys

from locators import LocatorsMainPage
from .login_page import LoginPage
from selenium.webdriver.common.by import By
from allure_steps import MainPageAllure
import allure


class MainPage(LoginPage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def check_1L_catalogs_are_present(self):
        with allure.step(MainPageAllure.USERS_DIR):
            self.wait_for_element(LocatorsMainPage.MP_USERS, by=By.XPATH, timeout=15)
            user_element = self.get_text(LocatorsMainPage.MP_USERS, by=By.XPATH)
            assert user_element == 'Пользователи', 'The actual name of catalog is ' + user_element \
                + ' and IT does not match the expected. Element should have name: "Пользователи"'

        with allure.step(MainPageAllure.OTHER_CATALOGS_DIR):
            self.is_element_present(LocatorsMainPage.MP_OTHER_CATALOGS, by="By.XPATH")
            other_catalog_element = self.get_text(LocatorsMainPage.MP_OTHER_CATALOGS, by=By.XPATH)
            assert other_catalog_element == 'Другие справочники', \
                'The actual name of catalog is ' + other_catalog_element + \
                ' and IT does not match the expected. Element should have name: "Другие справочники"'

        with allure.step(MainPageAllure.SALES_STUCTURE_DIR):
            self.is_element_present(LocatorsMainPage.MP_SALES_STUCTURE, by="By.XPATH")
            sales_structure_element = self.get_text(LocatorsMainPage.MP_SALES_STUCTURE, by=By.XPATH)
            assert sales_structure_element == 'Структура продаж', \
                'The actual name of catalog is ' + sales_structure_element + \
                ' and IT does not match the expected. Element should have name: "Структура продаж"'

        with allure.step(MainPageAllure.OUTLETS_DIR):
            self.is_element_present(LocatorsMainPage.MP_OUTLETS, by="By.XPATH")
            outlets_element = self.get_text(LocatorsMainPage.MP_OUTLETS, by=By.XPATH)
            assert outlets_element == 'Торговые точки', 'The actual name of catalog is ' + outlets_element + \
                ' and IT does not match the expected. Element should have name: "Торговые точки"'

        with allure.step(MainPageAllure.PRODUCTS_DIR):
            self.is_element_present(LocatorsMainPage.MP_PRODUCTS, by="By.XPATH")
            products_element = self.get_text(LocatorsMainPage.MP_PRODUCTS, by=By.XPATH)
            assert products_element == 'Продукция', 'The actual name of catalog is ' + products_element + \
                ' and IT does not match the expected. Element should have name: "Продукция"'

        with allure.step(MainPageAllure.DOCUMENTS_DIR):
            self.is_element_present(LocatorsMainPage.MP_DOCUMENTS, by="By.XPATH")
            documents_element = self.get_text(LocatorsMainPage.MP_DOCUMENTS, by=By.XPATH)
            assert documents_element == 'Документы', 'The actual name of catalog is ' + documents_element + \
                ' and IT does not match the expected. Element should have name: "Документы"'

        with allure.step(MainPageAllure.PLAN_AND_ANALYSE_DIR):
            self.is_element_present(LocatorsMainPage.MP_PLAN_AND_ANALYSE, by="By.XPATH")
            plan_analyse_element = self.get_text(LocatorsMainPage.MP_PLAN_AND_ANALYSE, by=By.XPATH)
            assert plan_analyse_element == 'План/Анализ', \
                'The actual name of catalog is ' + plan_analyse_element + \
                ' and IT does not match the expected. Element should have name: "План/Анализ"'

        with allure.step(MainPageAllure.REPORTS_DIR):
            self.execute_script("document.getElementById('" + LocatorsMainPage.MP_REPORTS_ID + "').scrollIntoView()")
            self.is_element_present(LocatorsMainPage.MP_REPORTS, by="By.XPATH")
            reports_element = self.get_text(LocatorsMainPage.MP_REPORTS, by=By.XPATH)
            assert reports_element == 'Отчеты', 'The actual name of catalog is ' + reports_element + \
                ' and IT does not match the expected. Element should have name: "Отчеты"'

        with allure.step(MainPageAllure.DATA_EXCHANGE_DIR):
            self.scroll_to(LocatorsMainPage.MP_DATA_EXCHANGE, by="By.XPATH")
            self.is_element_present(LocatorsMainPage.MP_DATA_EXCHANGE, by="By.XPATH")
            data_exchange_element = self.get_text(LocatorsMainPage.MP_DATA_EXCHANGE, by=By.XPATH)
            assert data_exchange_element == 'Обмен данными', 'The actual name of catalog is ' + data_exchange_element +\
                ' and IT does not match the expected. Element should have name: "Обмен данными"'

    def open_help_menu(self):
        self.find_element('//*[@id="Vertical_CallbackPanel_SAC_Menu_DXI1_T"]', by=By.XPATH)