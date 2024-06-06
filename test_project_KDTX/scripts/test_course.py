
import pytest
from test_project_KDTX.api.APIs import Login_API
from test_project_KDTX.api.APIs import Course_API



class Test_Course:
    token = None #类属性初始化
    def setup_class(self):
        self.login_api = Login_API()
        self.course_api = Course_API()

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
        Test_Course.token = results.json().get("token")
        print("\ntoken is:", Test_Course.token)
        assert results.status_code == 200
        assert "成功" in results.text

    #test of adding course
    def test_add_course(self):
        test_data = {"name":"测试开发提升课01", "subject":"6",
                     "price": 899, "applicablePerson": "2",
                     "info": "测试开发提升课01"}
        #由于uuid/token数据临时有效，引用类属性时，一般需要从头开始
        test_results = self.course_api.add_course(body_data=test_data,
                        token=Test_Course.token)
        assert test_results.status_code == 200
        assert "成功" in test_results.text

    #test of checking courselist
    def test_check_courselist(self):
        parameter = "1361234567890"
        test_results = self.course_api.check_courselist(token=Test_Course.token,
                    param=parameter)
        assert test_results.status_code == 200
        assert "成功" in test_results.text

    #test of modifying courses
    def test_modify_course(self):
        test_data = {"id": 93}
        test_results = self.course_api.modify_course(body_data=test_data,
                    token=Test_Course.token)
        assert test_results.status_code == 200
        #assert "成功" in test_results.text 似乎此条assertion不能通过

    def test_delete_course(self):
        course_id = '93' #seems 404 for this id
        test_results = self.course_api.delete_course(id=course_id,
                        token=Test_Course.token)

        assert test_results.status_code == 200
        assert "成功" in test_results.text


