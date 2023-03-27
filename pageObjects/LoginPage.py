from selenium.webdriver.common.by import By


class LoginPage:
    textbox_username_xpath = "//input[@placeholder='Email or Username']"
    textbox_password_xpath = "//input[@placeholder='Password']"
    button_login_xpath = "//button[normalize-space()='Sign In']"
    arrow_dropdown_button_xpath = "//i[@class='k-icon k-i-arrow-chevron-down']"
    button_Logout_xpath = "//body//app-root//div[@class='auty-header bg-color-white']//div//div[3]"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).click()
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).click()
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.arrow_dropdown_button_xpath).click()
        self.driver.find_element(By.XPATH, self.button_Logout_xpath).click()
