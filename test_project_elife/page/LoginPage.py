from selenium.webdriver.common.by import By

from test_project_elife.base.page_base import BasePage
from selenium import webdriver
#元素层
class LoginPage(BasePage):
    #no need to initialize because of inheritance
    def find_username_input(self):
        return self.driver.find_element(By.ID, "username")
    def find_password_input(self):
        return self.driver.find_element(By.ID, "password")
    def find_login_btn(self):
        return self.driver.find_element(By.ID, 'loginBtn')

class LoginHandle: #元素的处理

    def __init__(self):
        self.page = LoginPage()
    def input_username(self, username):
        self.page.find_username_input().clear()
        self.page.find_username_input().send_keys(username)
    def input_password(self, password):
        self.page.find_password_input().clear()
        self.page.find_password_input().send_keys(password)
    def click_login_btn(self):
        self.page.find_login_btn().click()

class LoginProxy: #业务流程，不同动作的组合

    def __init__(self):
        self.handle = LoginHandle()

    def login(self, username, password):
        self.handle.input_username(username)
        self.handle.input_password(password)
        self.handle.click_login_btn()


