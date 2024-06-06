
import pytest
from test_project_KDTX.api.APIs import Login_API
from test_project_KDTX.api.APIs import Contract_API




class Test_Contract:
    token = None #类属性初始化
    def setup_class(self):
        self.login_api = Login_API()
        self.contract_api = Contract_API()

    #test of get verify code success
    def test_get_verify_success(self):
        results = self.login_api.get_verify_code()
        assert results.status_code == 200

    #test of login success
    def test_login_success(self):
        verify_uuid = self.login_api.get_verify_code().json().get("uuid")
        #uuid也可以通过类属性输入
        login_data = {"username": "admin", "password": "HM_2023_test",
                      "code": "2", "uuid": verify_uuid}
        results = self.login_api.login(login_data)
        Test_Contract.token = results.json().get("token")
        print("\ntoken is:", Test_Contract.token)
        assert results.status_code == 200
        assert "成功" in results.text

    def test_add_contract(self):
        body_params = {"name":"测试888",
                       "phone": "13612341888",
                       "contractno": "HT10012004",
                       "subject": "6",
                       "courseId": 99,
                       "channel": "0",
                       "activityId": 77,
                       "filename": "/profile/upload/2023/01/05/86e5a3b8-b08c-470c-a17d-71375c3a8b9f.pdf"}
        test_results = self.contract_api.add_contract(token=Test_Contract.token,
                                                          body_data=body_params)
        assert test_results.status_code == 200
        assert '成功' in test_results.text

    def test_upload_contract(self):
        f =  open("../files/contractexample.pdf", "rb")
        test_results = self.contract_api.upload_contract(token=Test_Contract.token,
                                                         body_data=f)
        assert test_results.status_code == 200
        assert '成功' in test_results.text

    def test_check_contract_list(self):
        test_results = self.contract_api.check_contract_list(token=
                        Test_Contract.token)
        assert test_results.status_code == 200
        assert '成功' in test_results.text

    def test_delete_contract(self):
        id_params = {10950251898105098}
        test_results = self.contract_api.delete_contract(token=Test_Contract.token,
                        contract_id=id_params)
        assert test_results.status_code == 200
        assert '成功' in test_results.text

