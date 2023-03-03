import time

from selenium.webdriver.common.by import By


class EntitiesPage:
    select_source_dropdown_xpath = "//span[contains(text(),'Select Source')]"
    select_excel_file_item_xpath = "//span[contains(text(),'Excel Files')]"
    select_destination_dropdown_id = "k-bdfede3d-7cd2-4bb7-a2a8-0abe67239ff9"
    select_quickbook_online_item_xpath = "//span[contains(text(),'QuickBooks Online')]"
    select_source_app_dropdown_xpath = "//kendo-dropdownlist[@class='auty-search-dropdwon impact-dropdown fill-container k-widget k-dropdown ng-pristine ng-valid ng-touched']//span[@class='k-input']"
    select_file_upload_item_xpath = "//kendo-dropdownlist[@class='auty-search-dropdwon impact-dropdown fill-container k-widget k-dropdown ng-valid ng-touched ng-dirty']//span[@class='k-input']"
    select_source_entity_destination_dropdown_xpath = "//kendo-dropdownlist[@class='auty-search-dropdwon impact-dropdown fill-container k-widget k-dropdown ng-pristine ng-valid ng-touched']//span[@class='k-icon k-i-arrow-s']"
    select_source_customer_entity_destination_item_xpath = "//span[contains(text(),'Customers')]"

    def __init__(self, driver):
        self.driver = driver

    def select_Excel_file_item(self):
        self.driver.find_element(By.XPATH, self.select_source_dropdown_xpath).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.select_excel_file_item_xpath).click()

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).click()
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.arrow_dropdown_button_xpath).click()
        self.driver.find_element(By.XPATH, self.button_Logout_xpath).click()