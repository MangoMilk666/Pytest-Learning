from V4.page.LoginPage import LoginProxy
from V4.base.utils import UtilsDriver
import time
import pytest

class Test_login:
    def setup_class(self):
        #先实例化，找到元素和操作
        self.login_p = LoginProxy()
        UtilsDriver.get_driver().get("http://127.0.0.1/mgr/sign.html")

    def setup_method(self):
        UtilsDriver.get_driver().implicitly_wait(5)

    def teardown_method(self):
        try:
            alert = UtilsDriver.get_driver().switch_to.alert
            alert.accept()
        except:
            pass
        UtilsDriver.get_driver().refresh()
    def teardown_class(self):
        UtilsDriver.quit_driver()

    def test_UI_0001(self):
        self.login_p.login('', '88888888')
        alerttext = UtilsDriver.get_alerttext()
        print("能看到这条文字吗?\n")
        assert alerttext == '请输入用户名'

    def test_UI_0002(self):
        self.login_p.login('byhy', '')
        alerttext = UtilsDriver.get_alerttext()
        assert alerttext == '请输入密码'
    def test_UI_0003(self):
        self.login_p.login('byh', '88888888')
        alerttext = UtilsDriver.get_alerttext()
        assert  alerttext == '登录失败 : 用户名或者密码错误'
    def test_UI_0004(self):
        self.login_p.login('byhy', '8888888')
        alerttext = UtilsDriver.get_alerttext()
        assert alerttext == '登录失败 : 用户名或者密码错误'
    def test_UI_0005(self):
        self.login_p.login('byhy', '888888888')
        alerttext = UtilsDriver.get_alerttext()
        assert alerttext == '登录失败 : 用户名或者密码错误'
