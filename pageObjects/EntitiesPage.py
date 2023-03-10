import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class EntitiesPage:
    select_source_dropdown_xpath = "//span[contains(text(),'Select Source')]"
    select_excel_file_option_xpath = "//span[contains(text(),'Excel Files')]"
    select_destination_dropdown_xpath = "//span[contains(text(),'Select Destination')]"
    select_quickbook_online_option_xpath = "//span[contains(text(),'QuickBooks Online')]"
    select_source_app_dropdown_xpath = "//span[contains(text(),'Select how you want your Auty-mation to run')]"
    select_file_upload_option_xpath = "//span[contains(text(),'File Upload')]"
    select_source_entity_destination_dropdown_xpath = "//span[contains(text(),'Select The Action to be done')]"
    select_source_Customer_entity_destination_item_xpath = "//span[contains(text(),'Customers')]"
    select_use_workflow_button_xpath = "//button[normalize-space()='Use Workflow']"
    select_file_upload_button_cssselector = ".btn-connect.row-connect.ng-star-inserted"
    create_new_connection_popup_heading_xpath = "//h4[normalize-space()='Create New Connection']"
    popup_connection_name_textbox_field_id = "connection-name"
    # popup_select_file_upload_button_xpath = "//div[@aria-label='Select files...']"
    popup_file_upload_path_xpath = "//input[@name='files']"
    popup_complete_file_upload_button_xpath = "//button[@class='k-primary fill-container k-button']"
    Customer_excel_sheet_tab_selection_xpath ="//span[@title='Customers']"


    def __init__(self, driver):
        self.driver = driver

    def select_Excel_file_item(self):
        self.driver.find_element(By.XPATH, self.select_source_dropdown_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.select_excel_file_option_xpath).click()
        time.sleep(5)
        # ///////////////////////////////////////////////////Choose Destination //////////////////////////////
        self.driver.find_element(By.XPATH, self.select_destination_dropdown_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.select_quickbook_online_option_xpath).click()
        time.sleep(5)
        # ///////////////////////////////////////////////Source App Section////////////////////////////////////
        self.driver.find_element(By.XPATH, self.select_source_app_dropdown_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.select_file_upload_option_xpath).click()
        time.sleep(5)
        # /////////////////////////Choose destination to see relevant options below////////////////////////////
        self.driver.find_element(By.XPATH, self.select_source_entity_destination_dropdown_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.select_source_Customer_entity_destination_item_xpath).click()
        time.sleep(10)
        # /////////////////////////////////////Work Flow Button///////////////////////////////////////////////
        self.driver.find_element(By.XPATH, self.select_use_workflow_button_xpath).click()

    def source_file_Upload(self):
        self.driver.find_element(By.CSS_SELECTOR, self.select_file_upload_button_cssselector).click()
        time.sleep(5)
        # self.driver.find_element(By.XPATH, self.create_new_connection_popup_heading_xpath).
        self.driver.find_element(By.ID, self.popup_connection_name_textbox_field_id).click()
        time.sleep(8)
        self.driver.find_element(By.ID, self.popup_connection_name_textbox_field_id).clear()
        self.driver.find_element(By.ID, self.popup_connection_name_textbox_field_id).send_keys("Automation")
        time.sleep(10)
        self.driver.find_element(By.XPATH, self.popup_file_upload_path_xpath).send_keys("C:\\Users\\Kamran\\PycharmProjects\\AMTJJ\\TestData\\Autymate_Sample_Source_Data_File.xlsx")
        time.sleep(20)
        self.driver.find_element(By.XPATH, self.popup_complete_file_upload_button_xpath).click()

    def Customer_excel_sheet_Tab(self):
        self.driver.find_element(By.XPATH, self.Customer_excel_sheet_tab_selection_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.arrow_dropdown_button_xpath).click()
        self.driver.find_element(By.XPATH, self.button_Logout_xpath).click()
