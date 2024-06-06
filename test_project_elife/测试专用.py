import time


from test_project_elife.page.LoginPage import LoginProxy
from test_project_elife.page.DevicePage import DeviceProxy

login = LoginProxy()
device = DeviceProxy()
login.login("byhy", "sdfsdf")
device.add_new_device("存储柜测试", "111", "222")
time.sleep(2)
