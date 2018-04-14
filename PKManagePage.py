# coding=utf-8

from time import sleep
from selenium.webdriver.common.by import By
from PageObject.BasePage import BasePage

class PKManagePage(BasePage):
    '''
    pkgl manage page
    '''

    #element locator

    ID_BaseSetup = (By.ID,'7143823f-4c9f-4e82-a2d1-f5cca04fe1ec')

    # public function
    def clickBaseSetup(self):
        sleep(2)
        self._click_element(self.ID_BaseSetup)

    class PKSetupPage(BasePage):
        '''
        pk setup page
        '''

        #element locator
        ID_Frame = (By.XPATH,"//iframe[contains(@id,'layui-layer-iframe')]")
        ID_AddPK = (By.XPATH,"//A[@id='a_Add']")
        ID_PKName = (By.NAME,'b_Name')
        ID_Grade1 = (By.ID,'span_ceadbcb2-2906-4d9d-ad08-493a60b8947e')
        ID_Grade2 = (By.ID, 'span_21093e6d-64b9-485c-aeb6-69e4871459e0')
        ID_Grade3 = (By.ID, 'span_ad86f5e4-1203-4f64-a51b-94db481d27f8')

        ID_YesTy = (By.ID,'yesTy')
        ID_NoTy = (By.ID,'noTy')

        ID_SubmitButton = (By.ID,'submit')

        # public function
        # public function
        def clickAddPK(self):
            sleep(2)
            self._click_element(self.ID_AddPK)
            frame = self.driver.find_element(*self.ID_Frame)
            self.driver.switch_to.frame(frame)

        def inputPKName(self,pkName):
            '''
            :param pkName:
            :return:
            '''
            sleep(2)
            self._type(self.ID_PKName,pkName)

        def selectGrade(self,grade):
            '''
            select grade
            :param grade: 1 means grade one, 2 means grade two, 3 means grade three
            :return:
            '''
            sleep(2)
            if int(grade) == 1:
                self._click_element(self.ID_Grade1)
            elif int(grade) == 2:
                self._click_element(self.ID_Grade2)
            elif int(grade) == 3:
                self._click_element(self.ID_Grade3)
            else:
                raise ValueError('please select 1、2 or 3 ')
        def selectTy(self,yes_or_no):
            '''
            select ty
            :param yes_or_no:
            :return:
            '''
            sleep(2)
            if yes_or_no == 'yes':
                self._click_element(self.ID_YesTy)
            elif yes_or_no == 'no':
                self._click_element(self.ID_NoTy)
            else:
                raise ValueError('please select "yes" or "no" ')

        def clickSubmitButton(self):
            sleep(2)
            self._click_element(self.ID_SubmitButton)


        def deletePkSetup(self,pkName):
            '''
            delete the pk setup
            :param pkName:
            :return:
            '''
            sleep(4)
            xpath = "//td[text()='%(pkName)s']/following-sibling::td/a[@title='删除']"%{'pkName':pkName}
            ID_DeletePK = (By.XPATH,xpath)
            self._click_element(ID_DeletePK)
            sleep(2)
            ID_ConfirmDelete = (By.XPATH, "//a[text()='确定']")
            self._click_element(ID_ConfirmDelete)

