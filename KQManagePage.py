# coding=utf-8

from time import sleep
from selenium.webdriver.common.by import By
from PageObject.BasePage import BasePage

class KQManagePage(BasePage):

    # element locator
    ID_KQTimeManage = (By.ID,'d27215ee-22a3-4a04-a284-93bc51ea86d8')
    ID_NewWorkTime = (By.XPATH,"//div[@class='open-time add']")
    ID_StartTime = (By.ID,'starttime')
    ID_EndTime = (By.ID,'endtime')
    ID_frame_newWorkTime = (By.XPATH, "//iframe[contains(@id,'layui-layer')]")
    ID_frame_selectTime = (By.XPATH, "//iframe[contains(@hidefocus,'true')]")
    ID_InputHour = (By.XPATH, "//input[@class='tB']")
    ID_InputMinute = (By.XPATH, "//input[@class='tE']")
    ID_OKButton = (By.ID, "dpOkInput")
    ID_YesButton = (By.XPATH,"//input[@class='yes' and @value='确定']")

    # public function
    def clickKQTimeManage(self):
        sleep(2)
        self._click_element(self.ID_KQTimeManage)

    def clickNewWorkTime(self):
        sleep(3)
        self._click_element(self.ID_NewWorkTime)

    def selectWorkTime(self,startTime,endTime):
        '''
        select work time
        :param startTime:string object like: "hour:minute"
        :param endTime:string object like "hour:minute"
        :return:
        '''
        startHour = str(startTime).split(":")[0]
        startMinute = str(startTime).split(":")[-1]
        endHour = str(endTime).split(":")[0]
        endMinute = str(endTime).split(":")[-1]

        self._selectStartTime(startHour,startTime)
        self._selectEndTime(endHour,endTime)
        self._click_element(self.ID_YesButton)

    def _selectStartTime(self,hour,minute):
        sleep(3)
        frame_newWorkTime = self.driver.find_element(*self.ID_frame_newWorkTime)
        self._switch_to_frame(frame_newWorkTime)
        sleep(2)
        self._click_element(self.ID_StartTime)
        self._selectTime(hour,minute)
        self._switch_to_default()

    def _selectEndTime(self,hour,minute):
        sleep(3)
        frame_newWorkTime = self.driver.find_element(*self.ID_frame_newWorkTime)
        self._switch_to_frame(frame_newWorkTime)
        sleep(2)
        self._click_element(self.ID_EndTime)
        self._selectTime(hour, minute)
        self._switch_to_default()

    def _selectTime(self,hour,minute):
        '''
        select time
        :param hour:
        :param minute:
        :return:
        '''
        sleep(3)
        frame_selectTime = self.driver.find_element(*self.ID_frame_selectTime)
        self._switch_to_frame(frame_selectTime)
        sleep(2)
        self._type(self.ID_InputHour,hour)
        sleep(2)
        self._type(self.ID_InputMinute,minute)
        sleep(2)
        self._click_element(self.ID_OKButton)
        self._switch_to_default()







