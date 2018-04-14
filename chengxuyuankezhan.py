# coding=utf-8

from selenium import webdriver
from time import sleep
import unittest
from PageObject import LoginPage,IndexPage,BXManagePage,PKManagePage,EvaluationPage,KQManagePage

class BXManegeTest(unittest.TestCase):

    def setUp(self):
        opt = webdriver.ChromeOptions()
        opt.add_argument('disable-infobars')
        self.driver = webdriver.Chrome(chrome_options=opt)
        self.url = 'http://61.190.34.91:82'

    def test_01_addAreaSetup(self):
        loginPage = LoginPage(self.driver,url=self.url)
        indexPage = IndexPage(self.driver)

        loginPage.login('xfadmin', '111111')
        indexPage.clickBXManage()

        bxManagePage = BXManagePage(self.driver)
        # click repair setup
        bxManagePage.clickRepairSetup()

        repairSetupPage = bxManagePage.RepairSetUp(self.driver)
        #click add area button
        repairSetupPage.clickAddAreaButton()

        addAreaSetupSubPage = bxManagePage.AddAreaSetup(self.driver)
        addAreaSetupSubPage.addAreaSetup('fgk-name',('increase',2),'fgk-desc')
        sleep(5)

    def test_02_searchArea(self):
        loginPage = LoginPage(self.driver, url=self.url)
        indexPage = IndexPage(self.driver)

        loginPage.login('xfadmin', '111111')
        indexPage.clickBXManage()

        bxManagePage = BXManagePage(self.driver)
        # click repair setup
        bxManagePage.clickRepairSetup()

        repairSetupPage = bxManagePage.RepairSetUp(self.driver)
        repairSetupPage.searchArea('fgk-name')

        sleep(5)

    def test_03_deleteArea(self):
        loginPage = LoginPage(self.driver, url=self.url)
        indexPage = IndexPage(self.driver)

        loginPage.login('xfadmin', '111111')
        indexPage.clickBXManage()

        bxManagePage = BXManagePage(self.driver)
        # click repair setup
        bxManagePage.clickRepairSetup()

        repairSetupPage = bxManagePage.RepairSetUp(self.driver)
        repairSetupPage.deleteArea('fgk-name')

        sleep(5)

    def test_04_addPKSetup(self):
        loginPage = LoginPage(self.driver, url=self.url)
        indexPage = IndexPage(self.driver)

        loginPage.login('xfadmin', '111111')
        pkManagePage = PKManagePage(self.driver)
        # click pk manage
        indexPage.clickPKManage()
        # click base setup
        # pkManagePage.clickBaseSetup()

        pkSetupPage = pkManagePage.PKSetupPage(self.driver)
        pkSetupPage.clickAddPK()
        pkSetupPage.inputPKName('PKName-test')
        # select grade one
        pkSetupPage.selectGrade(1)
        pkSetupPage.selectTy('yes')
        pkSetupPage.clickSubmitButton()

        sleep(5)

    def test_05_deletePKSetup(self):
        loginPage = LoginPage(self.driver, url=self.url)
        indexPage = IndexPage(self.driver)

        loginPage.login('xfadmin', '111111')
        pkManagePage = PKManagePage(self.driver)
        # click pk manage
        indexPage.clickPKManage()

        pkSetupPage = pkManagePage.PKSetupPage(self.driver)
        pkSetupPage.deletePkSetup('PKName-test')

        sleep(5)

    def test_06_addIndicate(self):
        loginPage = LoginPage(self.driver, url=self.url)
        indexPage = IndexPage(self.driver)

        loginPage.login('xfadmin', '111111')
        evaluationPage = EvaluationPage(self.driver)
        #click evaluation
        indexPage.clickEvaluation()

        #click indicate manage
        evaluationPage.clickIndicateManege()
        addIndicatePage = evaluationPage.AddIndicatePage(self.driver)
        # click add indicate
        addIndicatePage.clickAddIndicateButton()

        # select indicate type:single
        # addIndicatePage.selectIndicateType(1)
        addIndicatePage.intutIndicateNameAndScore(('IndicateName-test',100))
        addIndicatePage.InputOptionsAndScore([('option-A',10),('option-B',20),('option-C',30),('option-D',40)])
        addIndicatePage.Sorting('increase',2)
        addIndicatePage.clickConfirmButton()

        sleep(5)

    def test_07_deleteIndecate(self):
        loginPage = LoginPage(self.driver, url=self.url)
        indexPage = IndexPage(self.driver)

        loginPage.login('xfadmin', '111111')
        evaluationPage = EvaluationPage(self.driver)
        # click evaluation
        indexPage.clickEvaluation()

        # click indicate manage
        evaluationPage.clickIndicateManege()
        addIndicatePage = evaluationPage.AddIndicatePage(self.driver)
        addIndicatePage.deleteIndicate('IndicateName-test')

        sleep(5)

    def test_08_addWorkTime(self):

        loginPage = LoginPage(self.driver, url=self.url)
        indexPage = IndexPage(self.driver)

        loginPage.login('xfadmin', '111111')
        indexPage.clickKQManage()

        kqManagePage = KQManagePage(self.driver)
        kqManagePage.clickKQTimeManage()
        kqManagePage.clickNewWorkTime()

        kqManagePage.selectWorkTime(startTime='09:30',endTime='18:00')
        sleep(5)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
