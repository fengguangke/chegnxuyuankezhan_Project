# coding=utf-8
from selenium.webdriver.common.by import By
from PageObject.BasePage import BasePage

class LoginPage(BasePage):
    '''
    login page
    '''

    # element locator
    ID_USERNAME = (By.ID,'T_userName')
    ID_PASSWORD = (By.ID,'T_password')
    ID_LOGIN_BUTTON = (By.XPATH,"//div[@class='button']/span")

    def __init__(self,driver,url):
        super(LoginPage, self).__init__(driver,url)
        self.open()

    # public function
    def inputUsername(self,username):
        self._type(self.ID_USERNAME,username)

    def inputPassword(self,password):
        self._type(self.ID_PASSWORD,password)

    def clickLoginButton(self):
        self._click_element(self.ID_LOGIN_BUTTON)

    def login(self,username,password):
        self.inputUsername(username)
        self.inputPassword(password)
        self.clickLoginButton()

