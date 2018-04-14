# coding=utf-8

from time import sleep
from selenium.webdriver.common.by import By
from PageObject.BasePage import BasePage

class BXManagePage(BasePage):
    """
    BX Manage page class
    """

    # element locator
    ID_RepairConfig = (By.ID,'23ac7c1a-592e-4d84-ae6c-d43d5ee3ec91')
    ID_RepairSetup = (By.ID,'4d954615-1730-4cd7-9127-26c932ae180f')
    ID_DeviceRepair = (By.ID,'f5188993-e65c-4346-9809-944026749d96')
    ID_RepairReview = (By.ID,'d973a83c-1104-40c1-ae55-0cc15d3fd50f')
    ID_RepairProcess = (By.ID,'5aef9897-38fa-4afe-8de7-1550f1c516d1')

    ID_SystemSetup = (By.XPATH,"//div[@class='bx-set-top']/a[text()='系统设置']")
    ID_DeviceRepairFieldsSetup = (By.XPATH,"//div[@class='bx-set-top']/a[text()='设备报修字段设置']")

    # public function

    def clickRepairConfig(self):
        self._click_element(self.ID_RepairConfig)

    def clickSystemSetup(self):
        self._click_element(self.ID_SystemSetup)

    def clickDeviceRepairFieldSetup(self):
        self._click_element(self.ID_DeviceRepairFieldsSetup)

    def clickDeviceRepair(self):
        self._click_element(self.ID_DeviceRepair)

    def clickRepairSetup(self):
        sleep(1)
        self._click_element(self.ID_RepairSetup)

    class SystemSetup(BasePage):
        """
        BX Manage page -> system setup subPage
        """

        # element locator
        ID_RepairRemark = (By.ID,'R_Remark')
        ID_IsBHYes = (By.ID,"isBHYes")
        ID_IsBHNo = (By.ID,'isBHNo')
        ID_DHQZ = (By.ID,'R_Dhqz')
        ID_IsYearYes = (By.ID,'isYearYes')
        ID_IsYearNo = (By.ID,'isYearNo')
        ID_R_Num = (By.ID,'R_Num')
        ID_SAVE_BUTTON = (By.XPATH,"//input[@class='save']")

        # public function
        def inputRepairRemark(self,repariRemark):
            '''
            input the repair market
            :param repariRemark:
            :return:
            '''
            self._type(self.ID_RepairRemark,repariRemark)

        def selectIsBH(self,yes_or_no):
            '''
            select is BH ,yew or no
            :param yes_or_no:
            :return:
            '''
            if yes_or_no == 'yes':
                self._click_element(self.ID_IsBHYes)
            elif yes_or_no == 'no':
                self._click_element(self.ID_IsBHNo)
            else:
                raise ValueError('please select "yes" or "no" ')

        def inputDHqz(self,dhqz):
            '''
            input the DHqz
            :param dhqz:
            :return:
            '''
            self._type(self.ID_DHQZ,dhqz)

        def selectIsYear(self,yes_or_no):
            '''
            select is year ,yes or no
            :param yes_or_no:
            :return:
            '''
            if yes_or_no == 'yes':
                self._click_element(self.ID_IsYearYes)
            elif yes_or_no == 'no':
                self._click_element(self.ID_IsYearNo)
            else:
                raise ValueError('please select "yes" or "no" ')

        def inputR_num(self,r_num):
            '''
            input the value of the R_num
            :param r_num:
            :return:
            '''
            self._type(self.ID_R_Num,r_num)

        def clickSaveButton(self):
            '''
            click the save button
            :return:
            '''
            self._click_element(self.ID_SAVE_BUTTON)

    class DeviceRepairFieldsSetup(BasePage):
        """
        BX Manage page -> device repair fields setup sub page
        """
        pass
        # TODO: DEVICE RAPAIR FIELDS SETUP PAGE

    class RepairSetUp(BasePage):
        '''
        repair setup page
        '''

        #elemet locator
        ID_AddAreaButton = (By.XPATH,"//a[@id='addArea']")
        ID_FilterAreaInput = (By.XPATH,"//input[@class='filter-input']")
        ID_SearchButton = (By.XPATH,"//a[@id='search']")

        def clickAddAreaButton(self):
            sleep(3)
            self._click_element(self.ID_AddAreaButton)

        def searchArea(self,areaName):
            '''
            search area name
            :param areaName:
            :return:
            '''
            sleep(1)
            self._type(self.ID_FilterAreaInput,areaName)
            sleep(1)
            self._click_element(self.ID_SearchButton)
            result_xpath = (By.XPATH,"//td[text()='%(areaName)s']"%{'areaName':areaName})
            result_element = self.driver.find_element(*result_xpath)
            if result_element:
                print('search area success')
            else:
                print('search area fail')

        def deleteArea(self,areaName):
            '''
            delete area
            :param areaName: the name of area
            :return:
            '''
            sleep(1)
            delete_xpath = "//td[text()='%(areaName)s']/following-sibling::td/a[@title='删除']"%{'areaName':areaName}
            ID_DeleteArea = (By.XPATH,delete_xpath)
            self._click_element(ID_DeleteArea)
            sleep(2)
            ID_ConfirmDelete = (By.XPATH,"//a[text()='确定']")
            self._click_element(ID_ConfirmDelete)

        def checkSearchResult(self,expectValue):
            '''
            check search results
            :param expectValue:
            :return:
            '''
            pass
            # TODO:CHECK SEARCH RESULTS

    class AddAreaSetup(BasePage):
        '''
        repair setup -> area setup sub page
        '''
        # element locator
        ID_Frame = (By.XPATH,"//iframe[contains(@id,'layui-layer-iframe')]")
        ID_R_AreaName = (By.ID,'R_AreaName')
        ID_SortIncrease = (By.XPATH,"//a[@class='increase']")
        ID_SortDecrease = (By.XPATH,"//a[@class='decrease']")
        ID_R_AreaRemark = (By.ID,"R_AreaRemark")
        ID_SureButton = (By.ID,'sure')

        # public function
        def __init__(self,driver,url=None):
            # super(AddAreaSetup, self).__init__(diver,url)
            BasePage.__init__(self,driver,url)
            frame = self.driver.find_element(*self.ID_Frame)
            self.driver.switch_to.frame(frame)

        def addAreaSetup(self,r_areaName,sort_step,r_areaRemark):
            '''
            add area setup
            :param r_areaName:
            :param sort_step: a list or tuple,like:(sort,step)
            :param r_areaRemark:
            :return:
            '''
            sleep(2)
            self.inputR_AreaName(r_areaName)
            sleep(1)
            self.sorting(*sort_step)
            sleep(1)
            self.inputR_AreaRemark(r_areaRemark)
            sleep(1)
            self.clickSureButton()

        def inputR_AreaName(self,r_areaName):
            self._type(self.ID_R_AreaName,r_areaName)

        def sorting(self,decrease_or_increase,step):
            '''
            click sort
            :param decrease_or_increase:
            :param step:
            :return:
            '''

            if decrease_or_increase == 'increase':
                for s in range(int(step)):
                    self._click_element(self.ID_SortIncrease)
                    sleep(1)
            elif decrease_or_increase == "decrease":
                for s in range(int(step)):
                    self._click_element(self.ID_SortDecrease)
                    sleep(1)
            else:
                raise ValueError("please select increase or decrease")

        def inputR_AreaRemark(self,r_areaRemark):
            self._type(self.ID_R_AreaRemark,r_areaRemark)

        def clickSureButton(self):
            self._click_element(self.ID_SureButton)




