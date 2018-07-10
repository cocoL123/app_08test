# __author: Honorbaby
# date: 2018/7/9
from selenium.webdriver.common.by import By

'''
首页
'''
#我的按钮

my_btn = (By.XPATH, "//*[contains(@text,'我的') and contains(@resource-id,'com.tpshop.malls:id/tab_txtv')]")
#登录按钮
login_btn = (By.ID, "com.tpshop.malls:id/nickname_txtv")
#用户账号
user_name_btn = (By.ID, "com.tpshop.malls:id/edit_phone_num")
#用户密码
user_pwd_btn = (By.ID, "com.tpshop.malls:id/edit_password")
#登录
login_btn_id = (By.ID, "com.tpshop.malls:id/btn_login")
# 登陆页面关闭按钮
login_close_page_id = (By.ID, "com.tpshop.malls:id/titlebar_back_imgv")
'''
个人中心
'''
#我的订单
my_order_btn = (By.XPATH, "//*[contains(@resource-id,'com.tpshop.malls:id/title_txtv') and contains(@text,'我的订单')]")
#设置按钮
setting_btn = (By.ID, "com.tpshop.malls:id/setting_btn")
'''
设置页面
'''
#安全退出按钮
exit_btn = (By.ID, "com.tpshop.malls:id/exit_btn")
