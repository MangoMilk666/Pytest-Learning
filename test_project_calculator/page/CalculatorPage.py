from selenium.webdriver.common.by import By

from test_project_calculator.base.page_base import BasePage


class CalculatorPage(BasePage): #后者包含创建driver方法

    def find_clear_btn(self):
        return self.driver.find_element(By.ID, 'simpleClearAllBtn')
    def find_plus_btn(self):
        return self.driver.find_element(By.ID, 'simpleAdd')
    def find_minus_btn(self):
        return self.driver.find_element(By.ID, 'simpleSubtr')
    def find_multiply_btn(self):
        return self.driver.find_element(By.ID, 'simpleMulti')
    def find_divide_btn(self):
        return self.driver.find_element(By.ID, 'simpleDivi')
    def find_num_btn(self, num):
        if (num == 0):
            return self.driver.find_element(By. ID, 'simple0')
        if (num == 1):
            return self.driver.find_element(By.ID, 'simple1')
        if (num == 2):
            return self.driver.find_element(By.ID, 'simple2')
        if (num == 3):
            return self.driver.find_element(By.ID, 'simple3')
        if (num==4):
            return self.driver.find_element(By.ID, 'simple4')
        if (num == 5):
            return self.driver.find_element(By.ID, 'simple5')
        if (num == 6):
            return self.driver.find_element(By.ID, 'simple6')
        if (num == 7):
            return self.driver.find_element(By.ID, 'simple7')
        if (num == 8):
            return self.driver.find_element(By.ID, 'simple8')
        if (num == 9):
            return self.driver.find_element(By.ID, 'simple9')
    def find_equal_btn(self):
        return self.driver.find_element(By.ID, 'simpleEqual')
    def find_result(self):
        return self.driver.find_element(By.ID, 'resultIpt')

class CalculatorHandle:
    def __init__(self):
        self.page = CalculatorPage()
    def click_clear(self):
        self.page.find_clear_btn().click()
    def click_plus(self):
        self.page.find_plus_btn().click()
    def click_minus(self):
        self.page.find_minus_btn().click()
    def click_multiply(self):
        self.page.find_multiply_btn().click()
    def click_divide(self):
        self.page.find_divide_btn().click()
    def click_num(self, num):
        self.page.find_num_btn(num).click()

    def click_equal(self):
        self.page.find_equal_btn().click()

    def get_result(self):
        return self.page.find_result().get_attribute("value")

    def get_digitlist(self, num): #将多位数从高位到低位的数字组成列表
        lst = []
        while (num != 0):
            digit = num % 10
            lst.insert(0, digit)
            num //= 10
        return lst


class CalculatorProxy:
    def __init__(self):
        self.cal_proxy = CalculatorHandle()
    def clear_result(self):
        self.cal_proxy.click_clear()
    def simple_plus(self, lst):
        index = 0
        for num in lst:
            digits = self.cal_proxy.get_digitlist(num)
            if (index == 0): #如果是第一个数，不用click '+'
                pass
            elif (index != 0): #后面的书相加要click '+'
                self.cal_proxy.click_plus()
            for digit in digits:
                self.cal_proxy.click_num(digit)
            index += 1
        self.cal_proxy.click_equal()
        result = self.cal_proxy.get_result()
        return result





