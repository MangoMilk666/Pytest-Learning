#网页计算器
#Implement tests in PO-mode and data-driven数据驱动
import time

import pytest
from test_project_calculator.base.utils import UtilsDriver
from test_project_calculator.page.CalculatorPage import CalculatorProxy
import json

def simple_plus_data():
    test_data = []
    with open("../data/simple_plus.json", encoding='UTF-8') as d:
        test_data = json.load(d)
    print("test_data=", test_data)
    return test_data #返回由json数据转换而成的二级列表
def tear_apart_num(num):
    '''
    对大于9的多位数进行处理,返回各个数字位上的数字
    '''
    digits = []
    while (num != 0):
        digits.insert(0, num % 10)
        num //= 10
    return digits


class Test_calculator:
    """
    针对网页计算器功能的测试类
    """
    def setup_class(self):
        self.cal_p = CalculatorProxy()
        #访问计算器url
        UtilsDriver.get_driver().get("http://cal.apple886.com/")

    def teardown_class(self):
        UtilsDriver.quit_driver()

    @pytest.mark.parametrize("test_data", simple_plus_data())
    def test_simple_plus(self, test_data): #将test_data的每个分量分别作为参数
        #及时清零
        self.cal_p.clear_result()
        #test_data is a list
        #大于9的数还要进行处理
        cal_data = test_data[0:-1]
        result = self.cal_p.simple_plus(cal_data)
        time.sleep(2)
        result = int(result)
        assert result == test_data[-1]







