import pytest
class LoginPage:
    username_id = "email"
    password_xpath = "//input[@id='pass']"
    Login_xpath = "//button[@name='login']"

    def __init__(self, driver):
        self.driver = driver

    def EnterUsername(self,uname):
        self.driver.find_element_by_id(self.username_id).send_keys(uname)


    def EnterPassword(self,pwd):
        self.driver.find_element_by_xpath(self.password_xpath).send_keys(pwd)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.Login_xpath).click()
