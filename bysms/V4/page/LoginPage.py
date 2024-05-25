#负责自动执行网页ui界面
from selenium import webdriver
import time
from V4.base.page_base import BasePage
from selenium.webdriver.common.by import By
#对象库层：定位元素
class LoginPage(BasePage):
    """
    登录页面
    """
    #def __init__(self):
        #self.driver = webdriver.Firefox()

    #进一步简化，甚至可以不用在各个Page类单独定义driver,直接建在BasePage类内即可

    def find_username(self): #找到用户名输入框
        return self.driver.find_element(By.ID, 'username')
    def find_password(self): #找到密码输入框
        return self.driver.find_element(By.ID, 'password')
    def find_login_btn(self): #找到‘登录’按钮
        return self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')

#操作层：对象从对象库层中拿
class LoginHandle:
    """
    在登陆界面进行的操作
    """
    def __init__(self):
        self.page = LoginPage()

    def input_username(self, username):
        self.page.find_username().clear()
        self.page.find_username().send_keys(username)
    def input_password(self, password):
        self.page.find_password().clear()
        self.page.find_password().send_keys(password)

    def click_login_btn(self):
        self.page.find_login_btn().click()

#业务层：调用操作层的东西
class LoginProxy:
    #封装操作层设置的登录动作
    def __init__(self):
        self.login_proxy = LoginHandle()
    def login(self, username, password):
        self.login_proxy.input_username(username)
        self.login_proxy.input_password(password)
        self.login_proxy.click_login_btn()






