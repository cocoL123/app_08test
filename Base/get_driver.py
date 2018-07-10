# __author: Honorbaby
# date: 2018/7/9
from appium import webdriver
def get_driver(package,activity):
    '''
        :param pac: 包名
        :param act: 启动名
        :return: 
        '''

    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps["platformVersion"] = "5.1"
    desired_caps["deviceName"] = "192.168.159.101:5555"
    desired_caps["appPackage"] = package
    desired_caps["appActivity"] = activity
    desired_caps["unicodeKeyboard"] = True
    desired_caps["resetKeyboard"] = True
    desired_caps['automationName'] = 'Uiautomator2'
    return webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)