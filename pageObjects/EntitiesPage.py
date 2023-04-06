import time
import re
from telnetlib import EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


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
    Customer_excel_sheet_tab_selection_xpath = "//span[@title='Customers']"
    next_step_button_in_flow_xpath = "//button[normalize-space()='Next']"
    Qbo_connection_button_xpath = "//span[contains(text(),'Click Here to Connect to Existing QuickBooks Onlin')]"
    Qbo_connection_button_setting_dropdown_cssselector = ".k-panelbar-item-text.ng-tns-c89-17.ng-star-inserted"
    Qbo_connection_popup_toggle_on_xpath = "//span[@class='k-switch-label-off']"
    Qbo_connection_popup_create_connection_button_cssselector = "span[class='ng-star-inserted']"
    Intuit_popup_Login_credentials_Email_xpath = "//input[@id='iux-username-password-sign-in-user-id-input']"
    Intuit_popup_Login_credentials_Password_id = "iux-username-password-sign-in-password-input"
    Intuit_popup_SignIn_button_cssselector = "button[type='submit']"
    Intuit_popup_Skip_now_button_xpath = "//button[normalize-space()='Skip for now']"
    Intuit_popup_Connecting_Autymate_to_QBO_button_cssselector = ".StyledButton__Wrapper-vnaxcc-1.gYvrJh.authorize-connect-button"
    next_3step_button_in_flow_xpath = "//button[normalize-space()='Next']"
    email_for_notification_4step_xpath = "//div[@fxlayout='column']//span//textarea"
    next_4step_button_in_flow_xpath = "//button[normalize-space()='Next']"
    next_5step_button_in_flow_xpath = "//button[normalize-space()='Next']"
    next_6step_button_in_flow_xpath = "//button[normalize-space()='Next']"
    edit_your_autymation_field_xpath = "//input[@class='k-input']"
    Run_Your_Autymation_button_xpath = "//div[@fxlayoutalign='center center']//button[@role='button']"
    Intuit_popup_email_selecting_button_xpath = "//span[normalize-space()='Email a code']"
    Intuit_popup_verification_code_continue_button_xpath = "//span[normalize-space()='Continue']"
    Review_validation_of_Enitity_Success_xpath = "//h4[normalize-space()='Success: 2']"
    Review_validation_of_Enitity_All_xpath = "//span[normalize-space()='All: 2']"
    Review_validation_of_Enitity_Failed_xpath = "//h4[normalize-space()='Failed: 0']"
    Review_validation_of_Enitity_page_button_Finish_xpath = "//button[normalize-space()='Finish']"
    select_source_Invoice_entity_destination_item_xpath = "//span[contains(text(),'Invoice')]"
    select_source_file_connection_entity_xpath = "(//span[@title='Autymate_Sample_Source_Data_File'][normalize-space()='Autymate_Sample_Source_ ...'])[1]"
    step1_entity_text_field_cssselector = "input[placeholder='Search...']"
    Invoice_excel_sheet_tab_selection_xpath = "//span[@title='Invoices']"
    Qbo_connection_Tab_selection_xpath = "(//span[@title='QuickBooks Online'][normalize-space()='QuickBooks Online'])[1]"
    Qbo_settings_Income_Account_New_Products_Services_xpath = "(//span[@id='bfcf91b9-391f-49b8-a0a0-399edab96413'])[1]"
    Qbo_settings_Expense_Account_New_Products_Services_xpath = "//div[@fxlayout='column']/div[@fxlayout='column']/div/div[@fxlayout='column']/div/app-auty-workflow-step/div[@fxlayout='column']/div[@fxlayout='row wrap']/div/div[@fxlayout='column']/div/app-auty-widget/div[@fxlayout='column']/div/form[@role='form']/formly-form/formly-field/app-auty-general-hub-query-settings-formly/app-auty-general-hub-query-settings/div[@fxflexlayout='row']/div[@fxflexlayout='row']/kendo-tabstrip/div[@role='tabpanel']/div/div/div[@fxlayout='row wrap']/div[1]/div[1]/kendo-dropdownlist[1]/span[@class='k-input']"
    Qbo_setting_discount_dropdown_option_cssselector = "#f5b6580c-4ddf-4b3e-ba2f-723993f10f01"
    Qbo_setting_advertising_dropdown_option_xpath = "//span[contains(text(),'Advertising')]"
    # Review_validation_of_Enitity_Counts_xpath ="//li[contains(@class,'k-state-default') and contains(@class,'k-state-active')]/span[contains(@class,'k-link') and contains(text(),'All')]"
    Invoice_Review_validation_of_Enitity_All_xpath = "//span[normalize-space()='All: 3']"
    Invoice_Review_validation_of_Enitity_Success_xpath = "//h4[normalize-space()='Success: 3']"
    Invoice_Review_validation_of_Enitity_Failed_xpath = "//h4[normalize-space()='Failed: 0']"



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

    def Customer_entity_selection(self):
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
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.next_step_button_in_flow_xpath).click()

    def QBO_connection_popup(self):
        self.driver.find_element(By.XPATH, self.Qbo_connection_button_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, self.Qbo_connection_button_setting_dropdown_cssselector).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.Qbo_connection_popup_toggle_on_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR,
                                 self.Qbo_connection_popup_create_connection_button_cssselector).click()

    def Intuit_popup_Login_Credentials(self):

        # Switch to the Intuit sign-in window
        intuit_window = self.driver.window_handles[1]
        self.driver.switch_to.window(intuit_window)

        self.driver.find_element(By.XPATH, self.Intuit_popup_Login_credentials_Email_xpath).click()
        self.driver.find_element(By.XPATH, self.Intuit_popup_Login_credentials_Email_xpath).send_keys(
            "termsorqbo+1@gmail.com")
        time.sleep(1)
        self.driver.find_element(By.ID, self.Intuit_popup_Login_credentials_Password_id).click()
        self.driver.find_element(By.ID, self.Intuit_popup_Login_credentials_Password_id).send_keys("Autotestk210#")
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, self.Intuit_popup_SignIn_button_cssselector).click()
        time.sleep(10)
        # self.driver.find_element(By.XPATH, self.Intuit_popup_Skip_now_button_xpath).click()
        # time.sleep(2)
        try:
            self.driver.find_element(By.XPATH, self.Intuit_popup_Skip_now_button_xpath).click()
        except NoSuchElementException:
            print("Element 1 not found. Moving to next step...")
        try:
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.Intuit_popup_email_selecting_button_xpath).click()
        except NoSuchElementException:
            print("Element 2 not found. Moving to next step...")
        pass
        '''
        try:
            time.sleep(5)
            self.driver.find_element(By.CSS_SELECTOR, self.Intuit_popup_Connecting_Autymate_to_QBO_button_cssselector).click()
        except NoSuchElementException:
            print("Element 3 not found. Moving to next step...")
        
        try:
            time.sleep(20)
            self.driver.find_element(By.XPATH, self.Intuit_popup_verification_code_continue_button_xpath).click()
        except NoSuchElementException:
            print("Element 4 not found. Moving to next step...")
        
        try:
            time.sleep(5)
            self.driver.find_element(By.XPATH, self.Intuit_popup_Skip_now_button_xpath).click()
        except NoSuchElementException:
            print("Element 5 not found. Moving to next step...")
        pass
        '''
        # Switch back to the original window
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[0])

    def Finishing_steps_flow(self):

        self.driver.find_element(By.XPATH, self.next_3step_button_in_flow_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.email_for_notification_4step_xpath).click()
        self.driver.find_element(By.XPATH, self.email_for_notification_4step_xpath).send_keys("automation@mailinator.com")
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.next_4step_button_in_flow_xpath).click()
        time.sleep(25)
        self.driver.find_element(By.XPATH, self.next_5step_button_in_flow_xpath).click()
        time.sleep(30)
        self.driver.find_element(By.XPATH, self.next_6step_button_in_flow_xpath).click()
        time.sleep(10)
        self.driver.find_element(By.XPATH, self.edit_your_autymation_field_xpath).click()
        self.driver.find_element(By.XPATH, self.edit_your_autymation_field_xpath).send_keys("Automation")
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.Run_Your_Autymation_button_xpath).click()

    def entity_validation_status_check(self):

        global all_count, success_count, failed_count
        try:
            all_count_element = self.driver.find_element(By.XPATH, self.Review_validation_of_Enitity_All_xpath)
            all_count_text = all_count_element.text
            all_count = int(all_count_text.split()[-1])
        except NoSuchElementException:
            print("All count not found")

        try:
            success_count_element = self.driver.find_element(By.XPATH, self.Review_validation_of_Enitity_Success_xpath)
            success_count_text = success_count_element.text
            success_count = int(success_count_text.split()[-1])
        except NoSuchElementException:
            print("Success count not found")

        try:
            failed_count_element = self.driver.find_element(By.XPATH, self.Review_validation_of_Enitity_Failed_xpath)
            failed_count_text = failed_count_element.text
            failed_count = int(failed_count_text.split()[-1])
        except NoSuchElementException:
            print("Failed count not found")

        # Compare the counts to the expected values and print the result
        if all_count == success_count and failed_count == 0:
            print("Test case passed")
        else:
            print("Test case failed")

                    ################################### Invoice ##############################################

    def Invoice_entity_selection(self):
        # /////////////////////////Choose destination to see relevant options below////////////////////////////
        self.driver.find_element(By.XPATH, self.select_source_entity_destination_dropdown_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.select_source_Invoice_entity_destination_item_xpath).click()
        time.sleep(10)
        # /////////////////////////////////////Work Flow Button///////////////////////////////////////////////
        self.driver.find_element(By.XPATH, self.select_use_workflow_button_xpath).click()

    def select_Source_file(self):

        self.driver.find_element(By.XPATH, self.select_source_file_connection_entity_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.next_step_button_in_flow_xpath).click()

    def Invoice_excel_sheet_Tab(self):

        self.driver.find_element(By.CSS_SELECTOR, self.step1_entity_text_field_cssselector).click()
        self.driver.find_element(By.CSS_SELECTOR, self.step1_entity_text_field_cssselector).send_keys("Invoice")
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.Invoice_excel_sheet_tab_selection_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.next_step_button_in_flow_xpath).click()

    def QBO_connection_Tab(self):

        self.driver.find_element(By.XPATH, self.Qbo_connection_Tab_selection_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.next_step_button_in_flow_xpath).click()
        time.sleep(10)
        # self.driver.find_element(By.XPATH, self.Qbo_settings_Income_Account_New_Products_Services_xpath).click()
        # time.sleep(5)
        # self.driver.find_element(By.CSS_SELECTOR, self.Qbo_setting_discount_dropdown_option_cssselector).click()
        # time.sleep(5)
        # self.driver.find_element(By.XPATH, self.Qbo_settings_Expense_Account_New_Products_Services_xpath).click()
        # time.sleep(5)
        # self.driver.find_element(By.XPATH, self.Qbo_setting_advertising_dropdown_option_xpath).click()


    def Invoice_entity_validation_status_check(self):

        global all_count, success_count, failed_count
        try:
            all_count_element = self.driver.find_element(By.XPATH, self.Invoice_Review_validation_of_Enitity_All_xpath)
            all_count_text = all_count_element.text
            all_count = int(all_count_text.split()[-1])
        except NoSuchElementException:
            print("All count not found")

        try:
            success_count_element = self.driver.find_element(By.XPATH, self.Invoice_Review_validation_of_Enitity_Success_xpath)
            success_count_text = success_count_element.text
            success_count = int(success_count_text.split()[-1])
        except NoSuchElementException:
            print("Success count not found")

        try:
            failed_count_element = self.driver.find_element(By.XPATH, self.Invoice_Review_validation_of_Enitity_Failed_xpath)
            failed_count_text = failed_count_element.text
            failed_count = int(failed_count_text.split()[-1])
        except NoSuchElementException:
            print("Failed count not found")

        # Compare the counts to the expected values and print the result
        if all_count == success_count and failed_count == 0:
            print("Test case passed")
        else:
            print("Test case failed")











