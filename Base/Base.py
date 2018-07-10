# __author: Honorbaby
# date: 2018/7/5
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self, driver):
        self.driver = driver

    def search_element(self,loc,timeout=10, poll=1.0):
        '''
        :param loc: 元组（元素定位方式，属性值）
        :param timeout: 
        :return: 
        '''
        return WebDriverWait(self.driver,timeout, poll).until(lambda x: x.find_element(*loc))

    def search_elements(self,loc,timeout=10, poll=1.0):
        '''
        :param loc: 元组（元素定位方式，属性值）
        :param timeout: 
        :return: 
        '''
        return WebDriverWait(self.driver,timeout,poll).until(lambda x: x.find_elements(*loc))

    def click_element(self,loc):
        self.search_element(loc).click()

    def input_element(self,loc,text):
        input_btn = self.search_element(loc)
        input_btn.clear()
        input_btn.send_keys(text)

    def get_toast(self, message):
        # 获取提示消息
        try:
            xpath = "//*[contains(@text,'{}')]".format(message)
            toast_message = self.search_element((By.XPATH, xpath), timeout=5, poll=0.1)
            return toast_message.text
        except Exception as e:
            return False