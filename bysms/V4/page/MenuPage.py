

from selenium.webdriver.common.by import By

from V4.base.page_base import BasePage


class MenuPage(BasePage):
    """
    对象库层：登录后的界面
    """
    #找到这些元素位置
    def find_customer_menu_btn(self): #使用xpath(带*号)真的可行？'//*[text()="药品"]'
        return self.driver.find_element(By.CSS_SELECTOR, 'a[href="#/customers"]')
    def find_medicine_menu_btn(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'a[href="#/medicines"]')
    def find_order_menu_btn(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'a[href="#/orders"]')

    def find_jump_to_byhynet(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'div.pull-right:nth-child(1) > a:nth-child(1)')

    def find_admin_btn(self):
        return  self.driver.find_element(By.CSS_SELECTOR, 'span.hidden-xs')

    def find_logout_btn(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'div.pull-right:nth-child(2) > a:nth-child(1)')
class MenuHandle:
        """
        操作层：针对菜单页面的操作
        """

        def __init__(self):
            self.page = MenuPage()
        #获取它们的文字
        def check_customer_menu(self):
            return self.page.find_customer_menu_btn().text

        def check_medicine_menu(self):
            return self.page.find_medicine_menu_btn().text

        def check_order_menu(self):
            return self.page.find_order_menu_btn().text

        def scroll_downward(self):
            js = "window.scrollTo(0, 1000)"
            self.page.driver.execute_script(js)

        def jump_to_official_net(self):
            self.page.find_jump_to_byhynet().click()

        def click_admin_btn(self):
            self.page.find_admin_btn().click()

        def click_logout_btn(self):
            self.page.find_logout_btn().click()

class MenuProxy:
    def __init__(self):
        self.menu_proxy = MenuPage()
        self.menu_handle = MenuHandle()
    def click_cus_menu(self):
        self.menu_proxy.find_customer_menu_btn().click()

    def click_medi_menu(self):
        self.menu_proxy.find_medicine_menu_btn().click()

    def click_order_menu(self):
        self.menu_proxy.find_order_menu_btn().click()

    def log_out(self):
        self.menu_handle.click_admin_btn()
        self.menu_handle.click_logout_btn()

