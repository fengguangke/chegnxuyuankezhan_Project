# coding=utf-8
"""
base page class
"""
from PageObject.ComLibrary import wait_visible_decorator

class BasePage(object):
    """base page"""
    def __init__(self,driver=None,base_url=""):
        self.driver = driver
        self.base_url = base_url


    # public function
    def open(self):
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(url=self.base_url)

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()

    def check_element_attribute(self,locator,attribute,expect_attribute):
        act_attribute = self._get_element_attribute(locator,attribute)
        if act_attribute != expect_attribute:
            raise AssertionError("the element '%s' attribute '%s' should be '%s',but"
                                 " in face it was '%s'."%(locator,attribute,expect_attribute,act_attribute))

    @wait_visible_decorator
    def element_should_be_exist(self,locator):
        element = self.driver.find_element(*locator)
        if not element:
            raise AssertionError("element with locator %s is not exists in current page..."%(",".join(locator)))

    def element_should_not_exist(self,locator):
        try:
            element = self.driver.find_element(*locator)
        except:
            return True
        if element:
            raise AssertionError("element with locator %s exists in current page..."%locator)

    def get_elements_counts(self,locator):
        """获取元素个数
        :param locator:tuple(By,value)
        :return counts:元素个数
        """
        try:
            elements = self.driver.find_elements(*locator)
            return len(elements)
        except:
            return 0

    # private
    @wait_visible_decorator
    def _click_element(self,locator):
        element = self.driver.find_element(*locator)
        element.click()

    @wait_visible_decorator
    def _type(self,locator,*value):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(*value)

    @wait_visible_decorator
    def _get_text(self,locator):
        element = self.driver.find_element(*locator)
        return element.text

    def _get_element_attribute(self,locator,attribute):
        element = self.driver.find_element(*locator)
        return element.get_attribute(attribute)

    def _js(self,script, *args):
        self.driver.execute_script(script,*args)

    def _switch_to_window(self,name_or_handle):
        self.driver.switch_to.window(name_or_handle)

    def _switch_to_frame(self,name_or_index_webelement):
        self.driver.switch_to.frame(name_or_index_webelement)

    def _switch_to_default(self):
        self.driver.switch_to.default_content()

    def save_screen_shot(self,filename=None):
        import os.path as path
        import os
        from time import time,sleep
        filename = "selenium-screenshot-%d.png"%int(time())
        full_path = path.join(os.getcwd(),"output_dir\%s"%filename)
        dir_name = path.dirname(full_path)
        try:
            os.mkdir(dir_name)
        except:
            pass

        save_flag = self.driver.get_screenshot_as_file(full_path)
        count = 1
        while not save_flag:
            if count >= 5:
                break;
            sleep(0.5)
            save_flag = self.driver.get_screenshot_as_file(full_path)
            count = count + 1