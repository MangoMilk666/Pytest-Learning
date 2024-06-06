import requests
#接口对象封装层
#requests库采用的参数:url, json(body为json参数), data(body为form参数)
#headers: Authorization
base_path = 'http://kdtx-test.itheima.net'

#登录相关:
class Login_API:
    def __init__(self):
        self.url_verify = base_path + "/api/captchaImage"
        self.url_login = base_path + "/api/login"

    #获取验证码接口
    def get_verify_code(self): #返回status_code, text和json等整体数据
        return requests.get(url=self.url_verify)
    #获取登录接口
    def login(self, body_data): #应输入整体数据
        return requests.post(url=self.url_login, json=body_data)

#课程相关
class Course_API:
    def __init__(self):
        self.login_api = Login_API()
        self.url_add_course = base_path + '/api/clues/course'
        self.url_check_course = base_path + '/api/clues/course/list'
        self.url_modify_course = base_path + '/api/clues/course'
        self.url_delete_course = base_path + '/api/clues/course/:id'


    #添加课程
    def add_course(self, body_data, token): #token as param in head(value of Authorization)
        return requests.post(url=self.url_add_course, headers={"Authorization": token}
                             , json=body_data)

    #查询课程列表
    def check_courselist(self, param, token):
        return requests.get(url=self.url_check_course, headers={"Authorization": token},
                            params=param)
    #修改课程
    def modify_course(self, body_data, token):
        return requests.put(url=self.url_modify_course, headers={"Authorization": token},
                            json=body_data)
    #删除课程
    def delete_course(self, token, id):
        #不要将课程ID作为参数写入requests；要将其放在URL后面
        return requests.delete(url=self.url_delete_course + f"/{id}", headers={"Authorization": token})

#合同相关
class Contract_API:
    def __init__(self):
        self.url_add_contract = base_path + '/api/contract'
        self.url_upload_contract = base_path + '/api/common/upload'
        self.url_check_contractlist = base_path + '/api/contract/list'
        self.url_delete_contract = base_path + '/api/contract/remove'

    #添加合同
    def add_contract(self, token, body_data):
        return requests.post(url=self.url_add_contract, headers={"Authorization": token},
                             json= body_data)
    #上传合同
    def upload_contract(self, token, body_data):
        return requests.post(url=self.url_upload_contract, headers= {"Authorization": token},
                             files={"file": body_data})

    #查看合同列表
    def check_contract_list(self, token): #不需要额外的参数
        return requests.get(url=self.url_check_contractlist, headers= {"Authorization": token})

    #删除合同
    def delete_contract(self, token, contract_id):
        return requests.post(url= self.url_delete_contract + f"/{contract_id}", headers={"Authorization": token})

#数据/对象层
#操作层
#业务/组合层