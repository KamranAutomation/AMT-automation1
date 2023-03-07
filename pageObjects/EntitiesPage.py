import time

from selenium.webdriver.common.by import By


class EntitiesPage:
    select_source_dropdown_xpath = "//span[contains(text(),'Select Source')]"
    select_excel_file_item_xpath = "//span[contains(text(),'Excel Files')]"
    select_destination_dropdown_xpath = "//span[contains(text(),'Select Destination')]"
    select_quickbook_online_item_xpath = "//span[contains(text(),'QuickBooks Online')]"
    select_source_app_dropdown_xpath = "//span[contains(text(),'Select how you want your Auty-mation to run')]"
    select_file_upload_item_xpath = "//span[contains(text(),'File Upload')]"
    select_source_entity_destination_dropdown_xpath = "//span[contains(text(),'Select The Action to be done')]"
    select_source_Customer_entity_destination_item_xpath = "//span[contains(text(),'Customers')]"
    select_use_workflow_button_xpath = "//span[normalize-space()='Use Workflow']"

    def __init__(self, driver):
        self.driver = driver

    def select_Excel_file_item(self):
        self.driver.find_element(By.XPATH, self.select_source_dropdown_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.select_excel_file_item_xpath).click()
        time.sleep(5)
        # ///////////////////////////////////////////////////Choose Destination //////////////////////////////
        self.driver.find_element(By.XPATH, self.select_destination_dropdown_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.select_quickbook_online_item_xpath).click()
        time.sleep(5)
        # ///////////////////////////////////////////////Source App Section////////////////////////////////////
        self.driver.find_element(By.XPATH, self.select_source_app_dropdown_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.select_file_upload_item_xpath).click()
        time.sleep(5)
        # /////////////////////////Choose destination to see relevant options below////////////////////////////
        self.driver.find_element(By.XPATH, self.select_source_entity_destination_dropdown_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.select_source_Customer_entity_destination_item_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.select_use_workflow_button_xpath).click()


    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).click()
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.arrow_dropdown_button_xpath).click()
        self.driver.find_element(By.XPATH, self.button_Logout_xpath).click()