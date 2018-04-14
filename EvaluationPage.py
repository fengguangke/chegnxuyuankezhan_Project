# coding=utf-8

from time import sleep
from selenium.webdriver.common.by import By
from PageObject.BasePage import BasePage

class EvaluationPage(BasePage):
    '''
    evaluation page
    '''

    # element locator
    ID_IndicateManage = (By.ID,'ab3628b8-9984-4ee9-bc22-3bdfadecb740')

    #public function
    def clickIndicateManege(self):
        sleep(2)
        self._click_element(self.ID_IndicateManage)

    class AddIndicatePage(BasePage):
        '''
        add indicate sub page
        '''

        #element locator
        ID_Frame = (By.XPATH, "//iframe[contains(@id,'layui-layer-iframe')]")
        ID_AddIndicateButton = (By.XPATH,"//a[@class='opr-btn add']")
        ID_IndicateTypeSingle = (By.XPATH,"//input[@value='1' and @name='f_type']")
        ID_IndicateTypeMulti = (By.XPATH, "//input[@value='2' and @name='f_type']")
        ID_IndicateTypeInput = (By.XPATH, "//input[@value='3' and @name='f_type']")
        ID_IndicateName = (By.NAME,'f_normName')
        ID_IndicateFullScore = (By.NAME,'f_str')
        ID_SortIncrease = (By.XPATH,"//a[@class='increase']")
        ID_SortDecrease = (By.XPATH,"//a[@class='decrease']")
        ID_SubmitButton = (By.ID,'submit')

        # public function
        def clickAddIndicateButton(self):
            sleep(2)
            self._click_element(self.ID_AddIndicateButton)
            frame = self.driver.find_element(*self.ID_Frame)
            self.driver.switch_to.frame(frame)

        def selectIndicateType(self,indicateType):
            '''
            select indicate type
            :param indicateType:1 means single,2 means multi, 3 means input
            :return:
            '''
            sleep(2)
            type_ = int(indicateType)
            if type_ == 1:
                self._click_element(self.ID_IndicateTypeSingle)
            elif type_ == 2:
                self._click_element(self.ID_IndicateTypeMulti)
            elif type_ == 3:
                self._click_element(self.ID_IndicateTypeInput)
            else:
                raise ValueError('please select 1、2 or3 ')

        def intutIndicateNameAndScore(self,indicateName_score):
            '''
            input the indicate and score
            :param indicateName_score:a tuple ,like(indicateName,score)
            :return:
            '''
            indicate,score = indicateName_score
            sleep(2)
            self._type(self.ID_IndicateName,indicate)
            sleep(2)
            self._type(self.ID_IndicateFullScore,score)

        def InputOptionsAndScore(self,optionScoreList):
            '''
            input four options and score
            :param scoreList:a list contains four (option,score) eg
            [('option-A',10),('option-B',20),('option-C',30),('option-D',40)]
            :return:
            '''
            sort = 0
            for idx,(option,score) in enumerate(optionScoreList):
                sleep(2)
                option_xpath = "//div[@data-sort='%d']/input[@name='explan']" %(idx+1)
                score_xpath = "//div[@data-sort='%d']/input[@name='score']" %(idx+1)
                ID_Option = (By.XPATH,option_xpath)
                ID_Score = (By.XPATH,score_xpath)
                self._type(ID_Option,option)
                sleep(2)
                self._type(ID_Score,score)

        def Sorting(self,increase_or_decrease,step):
            '''
            click sort
            :param increase_or_decrease:
            :param step:
            :return:
            '''
            sleep(2)
            if increase_or_decrease == 'increase':
                for s in range(int(step)):
                    self._click_element(self.ID_SortIncrease)
                    sleep(1)
            elif increase_or_decrease == "decrease":
                for s in range(int(step)):
                    self._click_element(self.ID_SortDecrease)
                    sleep(1)
            else:
                raise ValueError("please select increase or decrease")

        def clickConfirmButton(self):
            sleep(2)
            self._click_element(self.ID_SubmitButton)

        def deleteIndicate(self,indicateName):
            '''
            delete indicate
            :param indicateName:
            :return:
            '''
            sleep(2)
            del_xpath = "//td[text()='%(indicateName)s']/following-sibling::td/a[@class='td-opr-icon td-opr-last delete']"%{'indicateName':indicateName}
            ID_Delete = (By.XPATH,del_xpath)
            self._click_element(ID_Delete)
            sleep(2)
            ID_ConfirmDelete = (By.XPATH, "//a[text()='确定']")
            self._click_element(ID_ConfirmDelete)


