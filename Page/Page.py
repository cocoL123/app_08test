# __author: Honorbaby
# date: 2018/7/10
from Page.Login_Page import Login_Page
from Page.Setting_Page import Setting_Page

class Page:
    def __init__(self,driver):
        self.driver = driver

    def get_login_page(self):
        return Login_Page(self.driver)

    def get_setting_page(self):
        return Setting_Page(self.driver)