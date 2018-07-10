# __author: Honorbaby
# date: 2018/7/10
from Base.Base import Base
import Page,allure

class Setting_Page(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)

    def setting_page_btn(self):
        pass

    @allure.step(title="点击安全退出按钮")
    def setting_exit_btn(self):
        self.click_element(Page.exit_btn)