import time
from telnetlib import EC
import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.support.wait import WebDriverWait
from Utilities.customLogger import LogGen
from Utilities.readProperties import ReadConfig
from pageObjects.LoginPage import LoginPage


@allure.severity(allure.severity_level.NORMAL)
class Test_001_Login:
    baseURL = ReadConfig.getAppliactionURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @allure.severity(allure.severity_level.NORMAL)
    def test_homePageTitle(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Autymate":
            assert True
            self.driver.close()
        else:
            time.sleep(2)
            # self.driver.save_screenshot("./Screenshots/test_homePage1.png")
            self.driver.close()
            assert False

    @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self, setup):  # lp is stands for login page
        self.driver = setup
        self.driver.get(self.baseURL)
        time.sleep(5)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        act_title = self.driver.title
        print('current url', self.driver.current_url)
        print('title is ', act_title)
        if act_title == "Autymate":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("./Screenshots/test_login3.png")
            self.driver.close()
            assert False

    @allure.severity(allure.severity_level.CRITICAL)
    def test_logout(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(15)
        self.lp.clickLogout()
        time.sleep(2)
        if self.driver.current_url == "https://qa.autymate.com/account/login?product=amt-qbo":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("./Screenshots/test_logout4.png")
            self.driver.close()
            assert False

    def test_login1(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        # Wait for the dashboard page to load
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.title_contains("Autymate"))

        # Verify that the dashboard page is displayed
        assert "Autymate" in self.driver.title

        # Take a screenshot and close the browser window
        self.driver.save_screenshot("./Screenshots/test_login.png")
        self.driver.close()
