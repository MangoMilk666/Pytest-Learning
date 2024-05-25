from selenium import webdriver
from selenium.webdriver.common.by import By
from V4.base.page_base import BasePage
from V4.page.MenuPage import MenuProxy


class MedicinePage(BasePage):
    """
    对象库层：添加药品的界面
    """
    def find_addmed_btn(self): #添加药品按钮
        return self.driver.find_element(By.CSS_SELECTOR, 'button.btn-green')

    def find_med_name(self): #药品名称添加
        return self.driver.find_element(By.CSS_SELECTOR, ".col-lg-8 > div:nth-child(1) > input:nth-child(1)")

    def find_med_id(self): #药品id添加
        return self.driver.find_element(By.CSS_SELECTOR, '.col-lg-8 > div:nth-child(2) > input:nth-child(1)')

    def find_med_dscp(self): #药品描述添加
        return self.driver.find_element(By.CSS_SELECTOR, 'textarea.form-control')

    def find_do_create(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'button.btn-xs:nth-child(1)')
    def find_toplist_medname(self): #CSS_selector就不行??玄学...
        return self.driver.find_element(By.XPATH, '/html/body/div/div/section[2]/div[3]/div[1]/span[2]')

    def find_toplist_medid(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'div.search-result-item:nth-child(3) > div:nth-child(2) > span:nth-child(2)')

    def find_toplist_meddscp(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'div.search-result-item:nth-child(3) > div:nth-child(3) > span:nth-child(2)')

class MedicineHandle:
    """
    操作层：针对添加药品页面的操作
    """
    def __init__(self):
        self.page = MedicinePage()
    def click_add(self):
        self.page.find_addmed_btn().click()
    def input_medname(self, medname):
        self.page.find_med_name().clear()
        self.page.find_med_name().send_keys(medname)

    def input_medid(self, id):
        self.page.find_med_id().clear()
        self.page.find_med_id().send_keys(id)

    def input_meddscp(self, dscp):
        self.page.find_med_dscp().clear()
        self.page.find_med_dscp().send_keys(dscp)

    def click_create(self):
        self.page.find_do_create().click()
    def get_toplist_medname(self):
        return self.page.find_med_name().text
    def get_toplist_medid(self):
        return self.page.find_med_id().text
    def get_toplist_meddscp(self):
        return self.page.find_med_dscp().text


class MedicineProxy:
    """
    调用操作层的东西
    """
    def __init__(self):
        self.med_proxy = MedicineHandle()
        self.before_do = MenuProxy()
    #
    #先点击药品菜单，再执行添加药品名，编号，描述，点击创建四个动作
    def create_medicine(self, medname, id, dscp):
        self.before_do.click_medi_menu()
        self.med_proxy.click_add()
        self.med_proxy.input_medname(medname)
        self.med_proxy.input_medid(id)
        self.med_proxy.input_meddscp(dscp)
        self.med_proxy.click_create()

    def get_toplist_medname(self):
        return self.med_proxy.get_toplist_medname()
    def get_toplist_medid(self):
        return self.med_proxy.get_toplist_medid()
    def get_toplist_meddscp(self):
        return self.med_proxy.get_toplist_meddscp()

