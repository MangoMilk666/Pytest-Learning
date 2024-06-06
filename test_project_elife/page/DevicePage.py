import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_project_elife.base.page_base import BasePage

class DevicePage(BasePage):

    #no need of self-initialization
    def find_add_device_btn(self):
        return self.driver.find_element(By.XPATH, "/html/body/main/div[1]/span")

    def find_cancel_add_device_btn(self): #*此处添加与取消共用同一个元素位置，容易出错，因此每次添加完毕需要先取消再添加
        return self.driver.find_element(By.XPATH, '/html/body/main/div[1]/span')
    def find_storage_case(self):
        return self.driver.find_element(By.XPATH, '/html/body/main/div[1]/div/div[1]/select/option[1]')
    def find_ebike_charger(self):
        return self.driver.find_element(By.XPATH, '/html/body/main/div[1]/div/div[1]/select/option[2]')

    def find_carwashing_station(self):
        return self.driver.find_element(By.XPATH, '/html/body/main/div[1]/div/div[1]/select/option[3]')
    def find_auto_charger(self):
        return self.driver.find_element(By.XPATH, '/html/body/main/div[1]/div/div[1]/select/option[4]')

    def find_input_device_model(self):
        return self.driver.find_element(By.XPATH, '//*[@id="device-model"]')
    def find_input_device_desc(self):
        return self.driver.find_element(By.CSS_SELECTOR, '#device-model-desc')

    def find_confirm_adddevice_btn(self):
        return self.driver.find_element(By.XPATH, '/html/body/main/div[1]/div/div[4]/span')

    def find_toplist_device_type(self):
        return self.driver.find_element(By.XPATH, '/html/body/main/div[3]/div/div[1]/div[1]/span[2]')
    def find_toplist_device_model(self):
        return self.driver.find_element(By.XPATH, '/html/body/main/div[3]/div/div[1]/div[2]/span[2]')
    def find_toplist_device_desc(self):
        return self.driver.find_element(By.XPATH, "/html/body/main/div[3]/div/div[1]/div[3]/span[2]")

    def find_menu_device_model_btn(self):
        return self.driver.find_element(By.XPATH, '/html/body/ul/li[2]/a')

    #可以定义更综合性的函数，获取已添加设备列表中的设备类型/型号/描述/修改、删除列表
    # def find_first_page_device_info(self): #获取第一页上所有的已添加设备信息


class DeviceHandle:
    def __init__(self):
        self.page = DevicePage()
    def click_add_device_btn(self):
        self.page.find_add_device_btn().click()

    def click_cancel_add_device_btn(self):
        self.page.find_cancel_add_device_btn().click()
    def click_menu_device_model(self):
        self.page.find_menu_device_model_btn().click()
    def select_device_type(self, type):
        types = {"存储柜":self.page.find_storage_case(),
                 "电瓶车充电站": self.page.find_ebike_charger(),
                 "洗车站": self.page.find_carwashing_station(),
                 "汽车充电站": self.page.find_auto_charger()}

        types.get(type).click()

    def click_confirm_adddevice(self):
        self.page.find_confirm_adddevice_btn().click()

    def input_device_model(self, model):
        #self.page.find_input_device_model().clear() 此处clear似乎失效
        self.page.find_input_device_model().clear()
        self.page.find_input_device_model().send_keys(model)
    def input_device_desc(self, desc):
        self.page.find_input_device_desc().clear()
        self.page.find_input_device_desc().send_keys(desc)

    def get_toplist_device_type(self):
        return self.page.find_toplist_device_type().text
    def get_toplist_device_model(self):
        return self.page.find_toplist_device_model().text
    def get_toplist_device_desc(self):
        return self.page.find_toplist_device_desc().text


class DeviceProxy:
    def __init__(self):
        self.device_handle = DeviceHandle()
    def add_new_device(self, type, model, desc):
        self.device_handle.click_menu_device_model()
        self.device_handle.click_add_device_btn()
        self.device_handle.select_device_type(type)
        self.device_handle.input_device_model(model)
        self.device_handle.input_device_desc(desc)
        self.device_handle.click_confirm_adddevice()
        self.device_handle.click_cancel_add_device_btn() #先取消，下个用例再添加
    def get_toplist_device_type(self):
        return self.device_handle.get_toplist_device_type()

    def get_toplist_device_model(self):
        return self.device_handle.get_toplist_device_model()

    def get_toplist_device_desc(self):
        return self.device_handle.get_toplist_device_desc()




