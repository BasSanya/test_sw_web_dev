# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case(self):
        driver = self.driver
        driver.get(
            "https://appunileverdev.datacenter.ssbs.com.ua/SalesWorksWeb/Login.aspx?ReturnUrl=%2fSalesWorksWeb%2fdefault.aspx")
        driver.find_element_by_id("Logon_v0_28796466_MainLayoutEdit").click()
        driver.find_element_by_id("Logon_v0_28796466_MainLayoutEdit").click()
        driver.find_element_by_xpath(
            "//table[@id='Logon_v0_28796466_MainLayoutEdit_xaf_l38_xaf_dviPassword_Edit']/tbody/tr").click()
        driver.find_element_by_id("Logon_v0_28796466_MainLayoutEdit_xaf_l38_xaf_dviPassword_Edit_I").clear()
        driver.find_element_by_id("Logon_v0_28796466_MainLayoutEdit_xaf_l38_xaf_dviPassword_Edit_I").send_keys("")
        driver.find_element_by_id("Logon_v0_28796466_MainLayoutEdit_xaf_l38_xaf_dviPassword_Edit_I").clear()
        driver.find_element_by_id("Logon_v0_28796466_MainLayoutEdit_xaf_l38_xaf_dviPassword_Edit_I").send_keys(
            "%YvdvIjV28")
        driver.find_element_by_id("Logon_errorContainerCellId").click()
        driver.find_element_by_id("Logon_PopupActions_Menu_DXI0_T").click()
        driver.find_element_by_id("FavoriteCell").click()
        driver.find_element_by_id("FavoriteCell").click()
        driver.find_element_by_id("FavoriteCell").click()
        driver.find_element_by_id("FavoriteCell").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
