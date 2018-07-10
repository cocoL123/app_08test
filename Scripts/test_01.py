# __author: Honorbaby
# date: 2018/7/9
import pytest,sys,os,allure
sys.path.append(os.getcwd())
from Base.get_driver import get_driver
from Page.Page import Page
from Base.read_data import read_data


def get_data():
    data_list = []
    data = read_data("data.yml").read_yaml().get('Login_data')
    for i in data:
        for j in i.keys():
            data_list.append((j, i.get(j).get("phone"), i.get(j).get("passwd"),
                              i.get(j).get("get_mess"), i.get(j).get("expect_message"),
                              i.get(j).get("tag")))
    return data_list


class Test_01:

    def setup_class(self):
        self.Page_obj = Page(get_driver("com.tpshop.malls", ".SPMainActivity"))
        self.Page_obj.get_login_page().click_my_btn()

    def teardown_class(self):
        self.Page_obj.driver.quit()

    @allure.step("执行测试用例")
    @pytest.mark.parametrize("case_num, username, passwd,get_mess,expect_message, tag", get_data())
    def test_01_1(self,case_num, username, passwd, get_mess, expect_message, tag):
        self.Page_obj.get_login_page().click_sign_btn()
        self.Page_obj.get_login_page().input_mess(username,passwd)
        self.Page_obj.get_login_page().click_login_btn()
        if tag:
            try:
                order_status = self.Page_obj.get_login_page().if_my_order_status()
                toast = self.Page_obj.get_login_page().get_toast(get_mess)
                self.Page_obj.get_login_page().click_setting_btn()
                self.Page_obj.get_setting_page().clcik_exit_btn()
                assert order_status and toast == expect_message
            except Exception as e:
                print(e)
                self.Page_obj.get_login_page().click_close()
                assert False
        else:
            try:
                toast = self.Page_obj.get_login_page().get_toast(get_mess)
                if toast:
                    assert toast == expect_message
                else:
                    assert False
            finally:
                self.Page_obj.get_login_page().click_close()


