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
        with allure.step(MainPageAllure.FIND_HELP_BUTTON):
            self.find_element(LocatorsMainPage.HP_BUTTON, by=By.XPATH)
        with allure.step(MainPageAllure.CLICK_HELP_BUTTON):
            self.click(LocatorsMainPage.HP_BUTTON, by=By.XPATH)
        with allure.step(MainPageAllure.CHECK_HELP_MENU):
            assert self.assert_text('Добро пожаловать', LocatorsMainPage.HP_MESSAGE, by=By.XPATH), \
                'Help menu not open after click on help button'
        with allure.step(MainPageAllure.CHECK_HELP_LINK):
            assert self.get_attribute(LocatorsMainPage.HP_LINK, 'href', by=By.XPATH) ==\
                'http://helpsw.datacenter.ssbs.com.ua/SWEDocs/SWE/', 'Link for documentation not found or incorrect'

    def open_users_dir(self):
        with allure.step(MainPageAllure.SEARCH_DROP_MENU_USERS):
            self.find_element(LocatorsMainPage.US_DROP_MENU_USERS, by=By.XPATH)
        with allure.step(MainPageAllure.OPEN_DROP_MENU_USERS):
            self.click(LocatorsMainPage.US_DROP_MENU_USERS, by=By.XPATH)
        with allure.step(MainPageAllure.WAIT_DROP_MENU_USERS):
            self.wait_for_element_visible(LocatorsMainPage.US_DROP_MENU_SUB_USERS, by=By.XPATH)
        with allure.step(MainPageAllure.OPEN_DROP_MENU_OF_SUB_CATALOG_USERS):
            self.click(LocatorsMainPage.US_DROP_MENU_SUB_USERS, by=By.XPATH)

        with allure.step(MainPageAllure.USERS_SUB_DIR_OF_USERS):
            users_subdir = self.get_text(LocatorsMainPage.US_USERS_SUBDIR, by=By.XPATH)
            assert self.assert_text('Пользователи', LocatorsMainPage.US_USERS_SUBDIR, by=By.XPATH), \
                'Sub catalogs "Users" is not present of have incorrect name: ' + users_subdir

        with allure.step(MainPageAllure.TYPES_SUB_DIR_OF_USERS):
            users_type_dir = self.get_text(LocatorsMainPage.US_USERS_TYPE, by=By.XPATH)
            assert self.assert_text('Типы', LocatorsMainPage.US_USERS_TYPE, by=By.XPATH), \
                'Sub catalogs "Types" is not present of have incorrect name: ' + users_type_dir

        with allure.step(MainPageAllure.MM_USERS_SUB_DIR_OF_USERS):
            mm_users_dir = self.get_text(LocatorsMainPage.US_MM_USERS, by=By.XPATH)
            assert self.assert_text('Пользователи ММ', LocatorsMainPage.US_MM_USERS, by=By.XPATH), \
                'Sub catalogs "Mobile Modules Users" is not present of have incorrect name: ' + mm_users_dir

        with allure.step(MainPageAllure.MM_USERS_PROFILES_SUB_DIR_OF_USERS):
            mm_users_profile_dir = self.get_text(LocatorsMainPage.US_MM_USERS_PROFILES, by=By.XPATH)
            assert self.assert_text('Профили пользователей ММ', LocatorsMainPage.US_MM_USERS_PROFILES, by=By.XPATH), \
                'Sub catalogs "Mobile modules users profiles" is not present of have incorrect name: ' \
                + mm_users_profile_dir

        with allure.step(MainPageAllure.ABOUT_USER_SUB_DIR_OF_USERS):
            about_users_dir = self.get_text(LocatorsMainPage.US_ABOUT_USER, by=By.XPATH)
            assert self.assert_text('О пользователе', LocatorsMainPage.US_ABOUT_USER, by=By.XPATH), \
                'Sub catalogs "About user" is not present of have incorrect name: ' + about_users_dir

        with allure.step(MainPageAllure.LOGIN_TYPES_SUB_DIR_OF_USERS):
            login_types_dir = self.get_text(LocatorsMainPage.US_LOGIN_TYPES, by=By.XPATH)
            assert self.assert_text('Типы логинов', LocatorsMainPage.US_LOGIN_TYPES, by=By.XPATH), \
                'Sub catalogs "Login types" is not present of have incorrect name: ' + login_types_dir

        with allure.step(MainPageAllure.CLOSE_DROP_MENU_OF_SUB_USERS):
            self.click(LocatorsMainPage.US_CLOSE_SUB_MENU, by=By.XPATH)
        with allure.step(MainPageAllure.CLOSE_DROP_MENU_OF_USERS):
            self.click(LocatorsMainPage.US_CLOSE_MENU, by=By.XPATH)
            self.wait_for_element_not_visible(LocatorsMainPage.US_USERS_SUBDIR, by=By.XPATH)

    def open_other_dir(self):
        with allure.step(MainPageAllure.OPEN_DROP_MENU_OF_OTHER_CATALOGS):
            self.is_element_present(LocatorsMainPage.OT_OPEN_DROP_MENU_BTN, by=By.XPATH)
            self.click(LocatorsMainPage.OT_OPEN_DROP_MENU_BTN, by=By.XPATH)

        with allure.step(MainPageAllure.RESULT_OF_MM_SYNCHRON):
            synchronization_results = self.get_text('//*[@id="Vertical_NC_NB_I1i0_T"]/span', by=By.XPATH)
            assert self.assert_text('Результаты синхронизации ОО',
                                    '//*[@id="Vertical_NC_NB_I1i0_T"]/span', by=By.XPATH), \
                'Sub catalog "Result of Synchronization OO" is not present of have incorrect name: ' \
                + synchronization_results

        with allure.step(MainPageAllure.CLOSE_DROP_MENU_OF_OTHER_CATALOGS):
            self.click(LocatorsMainPage.OT_CLOSE_DROP_MENU_BTN, by=By.XPATH)
            self.wait_for_element_not_visible('//*[@id="Vertical_NC_NB_I1i0_T"]/span', by=By.XPATH)
