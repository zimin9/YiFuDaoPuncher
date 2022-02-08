# -*- encoding:utf-8 -*-

import requests
import json
from default_data import punch_in_data, accessToken

class punch_in_data_generator:
    def __init__(self):
        self.base_url = "https://yfd.ly-sky.com"
        self.header = {
            "accessToken": accessToken,
            "userAuthType": "MS"
        }
        self.check_in_index()

    def check_in_index(self):
        try:
            url = "/ly-pd-mb/form/api/healthCheckIn/client/stu/index"
            res = requests.get(self.base_url+url, headers=self.header)
            parse_data = json.loads(res.text)
            detail = dict.get(parse_data,"data")
            id = dict.get(detail,"questionnairePublishEntityId")        # 表单ID，每日不同
            filling_status = dict.get(detail, "hadFill")  # 填写状态
            if filling_status is False:
                print("请在手机上进行打卡后再运行此脚本")
            else:
                self.check_in_detail(str(id))
        except Exception as e:
            print(e)

    def check_in_detail(self,id):
        try:
            url = "/ly-pd-mb/form/api/questionnairePublish/" + str(id) + "/getDetailWithAnswer"
            res = requests.get(self.base_url+url,headers=self.header)
            parse_data = json.loads(res.text)
            data_list = dict.get(dict.get(parse_data, "data"),"answerInfoList")
            qpe_id = dict.get(dict.get(parse_data,"data"),"questionnairePublishEntityId")

            str_post_data = {}
            str_post_data["questionnairePublishEntityId"] = qpe_id
            str_post_data["answerInfoList"] = str(data_list).replace("null","None")

            f2 = open('punch_in_data.json', 'w')
            f2.write(str(str_post_data))
            f2.close()
        except Exception as e:
            print(e)

a = punch_in_data_generator()