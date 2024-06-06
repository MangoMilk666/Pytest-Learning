
import pytest
import json
from test_project_KDTX.api.APIs import Login_API

def get_test_data():
    with open("../data/login_testdata.json", encoding='UTF-8') as d:
        test_data = json.load(d)
    return test_data

class Test_Login:
    token = None #类属性初始化
    def setup_class(self):
        self.login_api = Login_API()
    #test of get verify code success
    def test_get_verify_success(self): #用不到参数
        results = self.login_api.get_verify_code()
        assert results.status_code == 200

    @pytest.mark.parametrize("test_data", get_test_data())
    def test_login_failure(self, test_data): #test_data读取后是字典形式
        verify_uuid = self.login_api.get_verify_code().json().get("uuid")
        #uuid也可以通过类属性输入
        login_data = {"username": test_data.get("username"),
                      "password": test_data.get("password"),
                      "code": test_data.get("code"),
                      "uuid": verify_uuid}
        results = self.login_api.login(login_data)
        Test_Login.token = results.json().get("token")
        print("\ntoken is:", Test_Login.token)
        assert results.status_code == 500
        assert "错误" in results.text

    def test_login_success(self):
        verify_uuid = self.login_api.get_verify_code().json().get("uuid")
        # uuid也可以通过类属性输入
        login_data = {"username": "admin",
                      "password": "HM_2023_test",
                      "code": "2",
                      "uuid": verify_uuid}
        results = self.login_api.login(login_data)
        Test_Login.token = results.json().get("token")
        print("\ntoken is:", Test_Login.token)
        assert results.status_code == 200
        assert "成功" in results.text






