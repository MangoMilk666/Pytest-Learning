import pytest
from test_project_elife.base.page_base import UtilsDriver
from test_project_elife.page.LoginPage import LoginProxy

class Test_login:
    def setup_class(self):
        self.login_p = LoginProxy()
        self.initial_url = "http://127.0.0.1:8234/login.html"
        UtilsDriver.get_driver().get(self.initial_url)

    def setup_method(self):
        UtilsDriver.get_driver().implicitly_wait(1)

    def teardown_method(self):
        try:
            alert = UtilsDriver.get_driver().switch_to.alert
            alert.accept()
        except:
            pass
        UtilsDriver.get_driver().refresh()

    def teardown_class(self):
        UtilsDriver.quit_driver()

    def test_SMP_login_002(self):  #用户名空白
        self.login_p.login("", "sdfsdf")
        alerttext = UtilsDriver.get_alerttext()
        assert alerttext == "请输入用户名"


    def test_SMP_login_003(self): #不输入密码
        self.login_p.login("byhy", "")
        alerttext = UtilsDriver.get_alerttext()
        assert alerttext == "请输入密码"


    def test_SMP_login_004(self): #输入错误密码,1 digit extra
        self.login_p.login("byhy", "sdfsdff")
        alerttext = UtilsDriver.get_alerttext()
        assert alerttext == "登录失败： 用户名或者密码错误"


    def test_SMP_login_005(self):  # 输入错误密码, 少1位
        self.login_p.login("byhy", "sdfsd")
        alerttext = UtilsDriver.get_alerttext()
        assert alerttext == "登录失败： 用户名或者密码错误"

    def test_SMP_login_006(self): #用户名错误，多1位
        self.login_p.login("byhyy", "sdfsdf")
        alerttext = UtilsDriver.get_alerttext()
        assert "用户名不存在" in alerttext

    def test_SMP_login_007(self): #用户名错误，少1位
        self.login_p.login("byh", "sdfsdf")
        alerttext = UtilsDriver.get_alerttext()
        assert "用户名不存在" in alerttext

    def test_SMP_login_001(self): #成功登录 因为url会变更，所以放在登录失败用例之后
        username = 'byhy'
        password = "sdfsdf"
        self.login_p.login(username, password)
        assert UtilsDriver.get_driver().current_url == "http://127.0.0.1:8234/index.html"


