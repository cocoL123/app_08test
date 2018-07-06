# __author: Honorbaby
# date: 2018/7/6
import pytest,allure


class Test_01:
    @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    def test_01_1(self):
        assert 0

    @allure.step('第一步')
    def test_01_1(self):
        allure.attach('描述', "我是第一步的描述")
        assert 1
