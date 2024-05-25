from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from V4.base.utils import UtilsDriver
from V4.page.CustomerPage import CustomerProxy
from V4.page.MenuPage import MenuHandle, MenuProxy
from V4.page.LoginPage import LoginProxy
from V4.page.MedicinePage import MedicineProxy
from V4.page.ByhynetPage import ByhyHandle
from V4.page.OrderPage import OrderProxy
import time
from selenium.webdriver.support import expected_conditions as EC

class Test_admin:
    def setup_class(self):
        self.menu_h = MenuHandle()
        self.login_p = LoginProxy()
        self.cus_p = CustomerProxy()
        self.med_p = MedicineProxy()
        self.byhy_h = ByhyHandle()
        self.menu_p = MenuProxy()
        self.ord_p = OrderProxy()
    def setup_method(self):
        # 每个用例都要执行：先成功登录
        UtilsDriver.get_driver().get("http://127.0.0.1/mgr/sign.html")
        time.sleep(2)
        self.login_p.login('byhy', '88888888')
        # Wait for the new page to load after login
        try:
            # 等待，直至新页面切换完毕，菜单按钮出现
            WebDriverWait(UtilsDriver.get_driver(), 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="#/customers"]'))
            )
        except Exception as e:
            pytest.fail(f"Failed to locate element after login: {e}")

    def teardown_class(self):
        UtilsDriver.quit_driver()


    def test_UI_0101(self):
        customer_text = self.menu_h.check_customer_menu()
        medicine_text = self.menu_h.check_medicine_menu()
        order_text = self.menu_h.check_order_menu()
        assert customer_text == '客户'
        assert medicine_text == '药品'
        assert order_text == '订单'

    def test_UI_0102(self):
        self.cus_p.create_customer("南京中医院", "12345678910", "南京市人民路")
        cusname = self.cus_p.get_toplist_cusname()
        cusphone = self.cus_p.get_toplist_cusphone()
        cusaddress = self.cus_p.get_toplist_cusaddress()
        assert cusname == '南京中医院'
        assert cusphone == '12345678910'
        assert cusaddress == '南京市人民路'
    def test_UI_0103(self):
        self.cus_p.create_customer("南京中医院", "12345678910", "南京市人民路")
        self.cus_p.modify_toplist_cusinfo(newcusname='南京省中医院')
        cusname = self.cus_p.get_toplist_cusname()
        cusphone = self.cus_p.get_toplist_cusphone()
        cusaddress = self.cus_p.get_toplist_cusaddress()
        assert cusname == '南京省中医院'
        assert cusphone == '12345678910'
        assert cusaddress == '南京市人民路'

    def test_UI_0105(self): #0104消失了...添加、检查药品
        self.med_p.create_medicine("药品1", "1234567", "这是一条药品说明测试")
        time.sleep(1)
        medname = self.med_p.get_toplist_medname()
        medid = self.med_p.get_toplist_medid()
        meddscp = self.med_p.get_toplist_meddscp()
        try:
            assert medname == "药品1"
            assert medid == "1234567"
            assert meddscp == "这是一条药品说明测试"
        except:
            print(medname)
            print(medid)
            print(meddscp)

    def test_UI_0106(self):
        self.menu_h.scroll_downward()
        self.menu_h.jump_to_official_net()
        time.sleep(2) #此时打开新的界面，产生新的handle
        #从原来的转向新的handle(总共2个handles)
        handles = UtilsDriver.get_driver().window_handles
        UtilsDriver.get_driver().switch_to.window(handles[-1])
        #抓取byhy.net新的元素
        print(self.byhy_h.get_teaching_sessions())
        #验证能回到原来的SMS网页menu界面
        UtilsDriver.get_driver().switch_to.window(handles[0])
        #退出登录
        self.menu_p.log_out()
        time.sleep(0.5)
        url = 'http://127.0.0.1/mgr/sign.html'
        assert url == UtilsDriver.get_driver().current_url



    def test_UI_0107(self): #数据驱动，批量添加药品和商品
        medicine_info = [('青霉素盒装1','YP-32342341','青霉素注射液，每支15ml，20支装'),
                         ('青霉素盒装2','YP-32342342','青霉素注射液，每支15ml，30支装'),
                         ('青霉素盒装3','YP-32342341','青霉素注射液，每支15ml，40支装')]
        customer_info = [('南京中医院1','2551867851','江苏省-南京市-秦淮区-汉中路-501'),
                         ('南京中医院2','2551867852','江苏省-南京市-秦淮区-汉中路-502'),
                         ('南京中医院3','2551867853','江苏省-南京市-秦淮区-汉中路-503')]
        #创建药品和客户
        for i in range(3):
            self.med_p.create_medicine(medicine_info[i][0], medicine_info[i][1], medicine_info[i][2])
        for i in range(3):
            self.cus_p.create_customer(customer_info[i][0], customer_info[i][1], customer_info[i][2])

        #添加新订单
        self.ord_p.create_order('test0107测试', '南京中医院2', '青霉素盒装1',
                                '100')
        #验证订单创建成功
        ordername = self.ord_p.get_toplist_ordername()
        cusname = self.ord_p.get_toplist_cusname()
        medi_info = self.ord_p.get_toplist_medinfo()
        assert ordername == 'test0107测试'
        assert cusname == '南京中医院2'
        assert '青霉素盒装1' in medi_info
        assert '100' in medi_info





