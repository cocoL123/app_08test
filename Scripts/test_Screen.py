# __author: Honorbaby
# date: 2018/7/10
import allure


class Test_Screen:

    def get_screen(self):
        with open("./Screen/test.png","rb") as f:
            allure.attach("图片名字",f.read(),allure.attach_type.PNG)

    def test_aa(self):
        allure.attach("描述","内容")
        assert 1,self.get_screen()

    def test_bb(self):
        assert False