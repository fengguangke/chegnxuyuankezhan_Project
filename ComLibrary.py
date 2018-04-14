# coding=utf-8

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import time
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException,TimeoutException

#****************decorator**************
def wait_visible_decorator(function):
    """
    decorator:wait element is visible
    """
    def wrap(self,locator,*args):
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located(locator))
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locator))
            return function(self,locator,*args)
        except NoSuchElementException:
            self.save_screen_shot()
            raise AssertionError("element with locator (%s) is not exist..."%(",".join(locator)))
        except (ElementNotVisibleException,TimeoutException):
            self.save_screen_shot()
            raise AssertionError("element with locator (%s) is not visible..."%(",".join(locator)))
    return wrap


def switchToSecondWindow(driver):
    cur_window = driver.current_window_handle
    win_handls = driver.window_handles
    for handle in win_handls:
        if handle != cur_window:
            driver.switch_to.window(handle)
            break



