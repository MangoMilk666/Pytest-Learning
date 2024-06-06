import time
from selenium import webdriver

class UtilsDriver:
    _driver = None
    @classmethod
    def get_driver(cls): #获取驱动
        if cls._driver is None:
            cls._driver = webdriver.Firefox()
            cls._driver.maximize_window()
            cls._driver.implicitly_wait(20) #隐式等待，全局范围生效
        return cls._driver
    @classmethod
    def quit_driver(cls): #退出驱动
        if cls._driver is not None:
            cls.get_driver().quit()
            cls._driver = None

    @classmethod
    def get_alerttext(cls):
        time.sleep(1)
        text = None
        try:
            text = cls.get_driver().switch_to.alert.text
        except:
            pass
        return text