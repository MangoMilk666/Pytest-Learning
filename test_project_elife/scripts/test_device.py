import time

from selenium import webdriver
from test_project_elife.page.LoginPage import LoginProxy
from test_project_elife.page.DevicePage import DeviceProxy
from test_project_elife.base.utils import UtilsDriver

class Test_device:
    def setup_class(self):
        self.login_p = LoginProxy()
        self.device_p = DeviceProxy()
        UtilsDriver.get_driver().get("http://127.0.0.1:8234/login.html")  # 要先登录，才能添加设备
        self.login_p.login("byhy", "sdfsdf")
    def setup_method(self):
        time.sleep(0.5)

    def teardown_method(self):
        pass

    def teardown_class(self):
        UtilsDriver.quit_driver()

    def test_device_model_001(self):
        device_type = "存储柜"
        device_model = "elife-canbinlocker-g22-10-20-40"
        device_desc = "南京e生活存储柜-10大20中40小"
        self.device_p.add_new_device(device_type, device_model, device_desc)

        check_type = self.device_p.get_toplist_device_type()
        check_model = self.device_p.get_toplist_device_model()
        check_desc = self.device_p.get_toplist_device_desc()
        assert check_type == device_type
        assert check_model == device_model
        assert check_desc == device_desc

    def test_device_model_002(self):
        device_type = "存储柜"
        device_model = ("一百个汉字如下哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈"
                        "哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈"
                        "哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈"
                        "哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈")
        device_desc = "南京e生活存储柜-10大20中40小"
        self.device_p.add_new_device(device_type, device_model, device_desc)

        check_type = self.device_p.get_toplist_device_type()
        check_model = self.device_p.get_toplist_device_model()
        check_desc = self.device_p.get_toplist_device_desc()
        assert check_type == device_type
        assert check_model == device_model
        assert check_desc == device_desc

    def test_device_model_101(self):
        device_type = "电瓶车充电站"
        device_model = "bokpower-charger-g22-220v450w"
        device_desc = "杭州bok 2022款450瓦 电瓶车充电站"
        self.device_p.add_new_device(device_type, device_model, device_desc)

        check_type = self.device_p.get_toplist_device_type()
        check_model = self.device_p.get_toplist_device_model()
        check_desc = self.device_p.get_toplist_device_desc()
        assert check_type == device_type
        assert check_model == device_model
        assert check_desc == device_desc

    def test_device_model_201(self):
        device_type = "洗车站"
        device_model = "njcw-carwasher-g22-2s"
        device_desc = "南京e生活2022款洗车机 2个洗车位"
        self.device_p.add_new_device(device_type, device_model, device_desc)

        check_type = self.device_p.get_toplist_device_type()
        check_model = self.device_p.get_toplist_device_model()
        check_desc = self.device_p.get_toplist_device_desc()
        assert check_type == device_type
        assert check_model == device_model
        assert check_desc == device_desc

    def test_device_model_301(self):
        device_type = "汽车充电站"
        device_model = "yixun-charger-g22-220v7kw"
        device_desc = "南京易迅能源2022款7千瓦汽车充电站"
        self.device_p.add_new_device(device_type, device_model, device_desc)

        check_type = self.device_p.get_toplist_device_type()
        check_model = self.device_p.get_toplist_device_model()
        check_desc = self.device_p.get_toplist_device_desc()
        assert check_type == device_type
        assert check_model == device_model
        assert check_desc == device_desc


    #def test_model_501(self):
        #前提：列表中只有一个型号为“电瓶车充电站”的设备
