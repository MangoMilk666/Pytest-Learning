import requests
import json
base_path = 'http://kdtx-test.itheima.net'
verify_url = base_path +'/api/captchaImage'
login_url = base_path + '/api/login'

dic = {"一":"11",
       "二": "22",
       "三": "33",
       "四": "44",
       "五": "55"}

print(dic.get("五"))