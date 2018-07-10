# __author: Honorbaby
# date: 2018/7/9
import allure
from Base.Base import Base
import Page


class Login_Page(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)

    @allure.step(title = "点击我的按钮")
    def click_my_btn(self):
        self.click_element(Page.my_btn)

    @allure.step(title = "点击登录注册")
    def click_sign_btn(self):
        self.click_element(Page.login_btn)

    @allure.step(title = "输入账号密码")
    def input_mess(self,username,userpwd):
        allure.attach("账号:","%s" % (username))
        allure.attach("密码:","%s" % (userpwd))
        self.input_element(Page.user_name_btn, username)
        self.input_element(Page.user_pwd_btn, userpwd)

    @allure.step(title = "点击登录按钮")
    def click_login_btn(self):
        self.click_element(Page.login_btn_id)

    @allure.step(title = "判断我的订单按钮是否存在")
    def if_my_order_status(self):
        allure.attch("存在:","True")
        allure.attch("不存在:","False")
        try:
            self.search_element(Page.my_order_btn)
            return True
        except Exception as e:
            assert False

    @allure.step(title = "点击设置按钮")
    def click_setting_btn(self):
        self.click_element(Page.setting_btn)

    @allure.step(title="点击关闭登录输入信息页面按钮")
    def click_close(self):
        self.click_element(Page.login_close_page_id)