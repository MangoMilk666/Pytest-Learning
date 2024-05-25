#负责订单管理页面元素定位
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from V4.base.page_base import BasePage
from V4.page.MenuPage import MenuProxy
from selenium.webdriver.common.keys import Keys

class OrderPage(BasePage):
    """
    对象库层：添加订单的界面
    """
    def find_addorder_btn(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.btn-md')

    def find_order_name(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".col-lg-8 > div:nth-child(1) > input:nth-child(1)")

    def find_select_cus(self):#选择客户的搜索框
        return self.driver.find_element(By.CSS_SELECTOR, '.col-lg-8 > div:nth-child(2) > input:nth-child(1)')

    def find_select_med(self): #选择药品的搜索框
        return self.driver.find_element(By.CSS_SELECTOR, '.col-lg-8 > div:nth-child(3) > input:nth-child(1)')

    def find_first_cus_result(self): #选择搜索客户的第一个结果（默认搜到）
        return self.driver.find_element(By.CSS_SELECTOR, 'select.xxx:nth-child(2) > option:nth-child(1)')

    def find_first_med_result(self): #选择搜索药品的第一个结果
        return self.driver.find_element(By.CSS_SELECTOR, '.col-lg-8 > div:nth-child(3) > select:nth-child(2) > option:nth-child(1)')

    def find_input_med_num(self): #设置药品数量
        return self.driver.find_element(By.XPATH, '/html/body/div[1]/div/section[2]/div[1]/div[1]/div[3]/div/input')

    def find_do_create_btn(self): #‘创建’按钮
        return self.driver.find_element(By.CSS_SELECTOR, 'button.btn-xs:nth-child(1)')

    def find_toplist_ordername(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'div.search-result-item:nth-child(3) > div:nth-child(1) > span:nth-child(2)')

    def find_toplist_order_cusname(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'div.search-result-item:nth-child(3) > div:nth-child(3) > span:nth-child(2)')

    def find_toplist_order_medicine(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'div.search-result-item:nth-child(3) > div:nth-child(4) > p:nth-child(2)')



class OrderHandle:
    """
    操作层：针对添加订单页面的操作
    """
    def __init__(self):
        self.page = OrderPage()
    def click_add(self):
        self.page.find_addorder_btn().click()
    def input_ordername(self, ordername):
        self.page.find_order_name().clear()
        self.page.find_order_name().send_keys(ordername)

    def select_customer(self, cus_name):
        self.page.find_select_cus().clear()
        self.page.find_select_cus().send_keys(cus_name)
        self.page.find_select_cus().send_keys(Keys.ENTER)


    def choose_cus_result(self):
        self.page.find_first_cus_result().click()

    def select_medicine(self, medi_name):
        self.page.find_select_med().clear()
        self.page.find_select_med().send_keys(medi_name)
        self.page.find_select_med().send_keys(Keys.ENTER)

    def choose_med_result(self):
        self.page.find_first_med_result().click()

    def set_medi_num(self, num):
        self.page.find_input_med_num().clear()
        self.page.find_input_med_num().send_keys(num)

    def click_create(self):
        self.page.find_do_create_btn().click()

    def get_toplist_ordername(self):
        return self.page.find_toplist_ordername().text
    def get_toplist_order_cusname(self):
        return self.page.find_toplist_order_cusname().text
    def get_toplist_order_medicine(self):
        return self.page.find_toplist_order_medicine().text


class OrderProxy:
    """
    调用操作层的东西
    """
    def __init__(self):
        self.order_proxy = OrderHandle()
        self.before_do = MenuProxy()

    #先点击订单菜单，再执行添加订单号码，订单名，选择客户，选择药品和数量，点击创建
    def create_order(self, ordername, cusname, mediname, medinum):
        self.before_do.click_order_menu()
        self.order_proxy.click_add()
        self.order_proxy.input_ordername(ordername)
        self.order_proxy.select_customer(cusname)
        self.order_proxy.choose_cus_result()

        self.order_proxy.select_medicine(mediname)
        self.order_proxy.choose_med_result()
        time.sleep(1)
        self.order_proxy.set_medi_num(medinum)
        self.order_proxy.click_create()


    def get_toplist_ordername(self):
        return self.order_proxy.get_toplist_ordername()
    def get_toplist_cusname(self):
        return self.order_proxy.get_toplist_order_cusname()
    def get_toplist_medinfo(self):
        return self.order_proxy.get_toplist_order_medicine()

