from selenium import webdriver
from selenium.webdriver.common.by import By
from V4.base.page_base import BasePage
from V4.page.MenuPage import MenuProxy


class CustomerPage(BasePage):
    """
    对象库层：添加客户的界面
    """
    def find_addcus_btn(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'button.btn-green')

    def find_cus_name(self):
        return self.driver.find_element(By.CSS_SELECTOR, "html>body>div>div>section>div>div>div:first-child>input")

    def find_cus_phone(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'html>body>div>div>section>div>div>div:nth-child(2)>input')

    def find_cus_address(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'html>body>div>div>section>div>div>div:nth-child(3)>textarea')

    def find_do_create(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'button.btn-xs:nth-child(1)')
    def find_toplist_cusname(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'div.search-result-item:nth-child(3) > div:nth-child(1) > span:nth-child(2)')

    def find_toplist_cusphone(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'div.search-result-item:nth-child(3) > div:nth-child(2) > span:nth-child(2)')

    def find_toplist_cusaddress(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'div.search-result-item:nth-child(3) > div:nth-child(3) > span:nth-child(2)')
    def find_modify_btn(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'div.search-result-item:nth-child(3) > div:nth-child(4) > div:nth-child(1) > label:nth-child(1)')
    def find_modify_cusname(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'div.search-result-item:nth-child(3) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)')
    #有需求还可定义：
    #def find_modify_cusphone
    #def find_modify_cusaddress
    def find_modify_confirm_btn(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'div.search-result-item-actionbar:nth-child(2) > div:nth-child(1) > label:nth-child(1)')
class CustomerHandle:
    """
    操作层：针对添加客户页面的操作
    """
    def __init__(self):
        self.page = CustomerPage()
    def click_add(self):
        self.page.find_addcus_btn().click()
    def input_cusname(self, cusname):
        self.page.find_cus_name().clear()
        self.page.find_cus_name().send_keys(cusname)

    def input_cusphone(self, phonenum):
        self.page.find_cus_phone().clear()
        self.page.find_cus_phone().send_keys(phonenum)

    def input_cusaddress(self, address):
        self.page.find_cus_address().clear()
        self.page.find_cus_address().send_keys(address)

    def click_create(self):
        self.page.find_do_create().click()
    def get_toplist_cusname(self):
        return self.page.find_toplist_cusname().text
    def get_toplist_cusphone(self):
        return self.page.find_toplist_cusphone().text
    def get_toplist_cusaddress(self):
        return self.page.find_toplist_cusaddress().text
    def click_modify(self):
        self.page.find_modify_btn().click()
    def modify_toplist_cusname(self, newcusname):
        if newcusname != self.page.find_modify_cusname().text:
            self.page.find_modify_cusname().clear()
            self.page.find_modify_cusname().send_keys(newcusname)
    #有需求还可定义：
    #def modify_toplist_cusphone
    #def modify toplist cusaddress
    def click_modify_confirm(self):
        self.page.find_modify_confirm_btn().click()





class CustomerProxy:
    """
    调用操作层的东西
    """
    def __init__(self):
        self.cus_proxy = CustomerHandle()
        self.before_do = MenuProxy()
    #
    #先点击客户菜单，再执行添加客户名，电话，住址，点击创建四个动作
    def create_customer(self, cusname, cusphone, cusaddress):
        self.before_do.click_cus_menu()
        self.cus_proxy.click_add()
        self.cus_proxy.input_cusname(cusname)
        self.cus_proxy.input_cusphone(cusphone)
        self.cus_proxy.input_cusaddress(cusaddress)
        self.cus_proxy.click_create()
    def get_toplist_cusname(self):
        return self.cus_proxy.get_toplist_cusname()
    def get_toplist_cusphone(self):
        return self.cus_proxy.get_toplist_cusphone()
    def get_toplist_cusaddress(self):
        return self.cus_proxy.get_toplist_cusaddress()
    def modify_toplist_cusinfo(self, newcusname): #有需求还可修改cusphone, cusaddress
        self.cus_proxy.click_modify()
        self.cus_proxy.modify_toplist_cusname(newcusname)
        #点击确认
        self.cus_proxy.click_modify_confirm()

