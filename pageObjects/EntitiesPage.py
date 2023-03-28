import time
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
    email_for_notification_4step_cssselector = ".margin-top-5.fill-container.ng-pristine.ng-valid.k-textarea.k-autofill.ng-touched"
    next_4step_button_in_flow_xpath = "//button[normalize-space()='Next']"
    next_5step_button_in_flow_xpath = "//button[normalize-space()='Next']"
    next_6step_button_in_flow_xpath = "//button[normalize-space()='Next']"
    edit_your_autymation_field_xpath = "//input[@class='k-input']"
    Run_Your_Autymation_button_xpath = "//div[@fxlayoutalign='center center']//button[@role='button']"
    Intuit_popup_email_selecting_button_xpath = "//span[normalize-space()='Email a code']"
    Intuit_popup_verification_code_continue_button_xpath = "//span[normalize-space()='Continue']"

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
        self.driver.find_element(By.CSS_SELECTOR, self.email_for_notification_4step_cssselector).click()
        self.driver.find_element(By.CSS_SELECTOR, self.email_for_notification_4step_cssselector).send_keys("automation@mailinator.com")
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

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.arrow_dropdown_button_xpath).click()
        self.driver.find_element(By.XPATH, self.button_Logout_xpath).click()
