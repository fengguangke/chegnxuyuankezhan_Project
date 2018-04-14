# coding=utf-8
from time import sleep
from selenium.webdriver.common.by import By
from PageObject.BasePage import BasePage
from PageObject.ComLibrary import switchToSecondWindow

class IndexPage(BasePage):
    '''
    index pages class
    '''

    # element locator
    ID_BX = (By.XPATH,"//a[@href='/BX/BX/Index/BX']")
    ID_PKGL = (By.XPATH,"//a[@href='/PK/PK/Index/PKGL']")
    ID_Evaluation = (By.XPATH,"//a[@href='/Evaluation/Evaluation/index/Evaluation']")
    ID_KQManage = (By.XPATH,"//a[@href='/KQ/KQ/index/KQ']")

    #public function
    def clickBXManage(self):
        sleep(3)
        self._click_element(self.ID_BX)

    def clickPKManage(self):
        sleep(3)
        self._click_element(self.ID_PKGL)
        switchToSecondWindow(self.driver)

    def clickEvaluation(self):
        sleep(3)
        self._click_element(self.ID_Evaluation)

    def clickKQManage(self):
        sleep(3)
        self._click_element(self.ID_KQManage)

    

