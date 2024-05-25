import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class UtilsDriver: #工具类
    _driver = None #给一个默认值，防止打开一堆浏览器;不想让外部看见方法/属性，加下划线
    #定义获取浏览器驱动的方法
    @classmethod
    def get_driver(cls):
        if cls._driver is None:
            cls._driver = webdriver.Firefox()
            cls._driver.maximize_window()
            cls._driver.implicitly_wait(20)
        return cls._driver

    #定义退出浏览器驱动的方法
    @classmethod
    def quit_driver(cls):
        #值为None时退出
        if cls._driver is not None:
            cls.get_driver().quit()
            cls._driver = None

    @classmethod
    def get_alerttext(cls):
        time.sleep(1)
        text = None
        try:
            text = cls._driver.switch_to.alert.text
        except:
            pass
        return text
    #还可以构造函数读取数据，设置日志器