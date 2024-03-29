import time
from selenium.webdriver.common.by import By
from telnetlib import EC
import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.support.wait import WebDriverWait
from Utilities.customLogger import LogGen
from Utilities.readProperties import ReadConfig
from pageObjects.LoginPage import LoginPage
from pageObjects.EntitiesPage import EntitiesPage


@allure.severity(allure.severity_level.NORMAL)
class Test_001_Entities:
    baseURL = ReadConfig.getAppliactionURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @allure.severity(allure.severity_level.CRITICAL)
    def test_Customer_entity(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.ep = EntitiesPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(10)
        self.ep.select_Excel_file_item()
        time.sleep(5)
        self.ep.Customer_entity_selection()
        time.sleep(10)
        self.ep.source_file_Upload()
        time.sleep(50)
        self.ep.Customer_excel_sheet_Tab()
        time.sleep(8)
        self.ep.QBO_connection_popup()
        time.sleep(30)
        self.ep.Intuit_popup_Login_Credentials()
        time.sleep(10)
        self.ep.Finishing_steps_flow()
        time.sleep(30)
        self.ep.entity_validation_status_check()
        time.sleep(5)
        self.lp.clickLogout()

    @allure.severity(allure.severity_level.CRITICAL)
    def test_Invoice_entity(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.ep = EntitiesPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(10)
        self.ep.select_Excel_file_item()
        time.sleep(5)
        self.ep.Invoice_entity_selection()
        time.sleep(5)
        self.ep.select_Source_file()
        time.sleep(8)
        self.ep.Invoice_excel_sheet_Tab()
        time.sleep(3)
        self.ep.QBO_connection_Tab()
        time.sleep(5)
        self.ep.Finishing_steps_flow()
        time.sleep(30)
        self.ep.Invoice_entity_validation_status_check()
        time.sleep(5)
        self.lp.clickLogout()
