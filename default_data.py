## 通知推送类型
## 可选：DingDing / Mail / None
notify = "DingDing"

## 钉钉机器人配置:
# access_token
dingding_access_token = "9b121xxxxxxxxxxxxxx508be80a2097xxxxxxxxx"
# secret
dingding_secret = "SEC324xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx260243754ac07708ebb905"

## 邮箱配置：
# 发信人
mail_sender = "cxxxxxxxx@163.com"
# 授权码
mail_auth_code = "CxxxxxxxxxJO"
# 收件人
mail_receiver = ["3xxxxxxx99@qq.com"]
# smtp地址
mail_smtp_link = "smtp.163.com"
# smtp端口
mail_smtp_port = 465

## 打卡信息配置：
# 打卡的accessToken
accessToken = "tW4ATw/+dOxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxmJuyfpfYcAsuSnOn2chlDaLo8r+hMVBStA1O2JxotiyzEJBxxxxxxxxxxxxxxxxxTxV/ZQ2kjxfYjqsaw/M9AiZ2Glqg=="
# 打卡数据
punch_in_data = {
    "questionnairePublishEntityId": "1001640744275339000980000000001",
    "answerInfoList": [
        {
            "subjectId": "1001640315554537000980000000001",
            "subjectType": "multiSelect",
            "multiSelect": {
                "optionAnswerList": [
                    {
                        "beSelectValue": "NotThing",
                        "fillContent": ""
                    }
                ]
            }
        },
        {
            "subjectId": "1001640315554577000980000000001",
            "subjectType": "location",
            "location": {
                "deviationDistance": 10000,
                "locationRangeId": "1001640054768198000150000000001",
                "address": "广东省广州市海珠区仑头路广东财经大学",
                "city": "广州市",
                "province": "广东省",
                "area": "海珠区",
                "latitude": 23.091564888,
                "longitude": 113.35413091
            }
        },
        {
            "subjectId": "1001640743741123000960000000001",
            "subjectType": "signleSelect",
            "signleSelect": {
                "beSelectValue": "flag1640743720931",
                "fillContent": ""
            }
        },
        {
            "subjectId": "1001640743758116001000000000001",
            "subjectType": "signleSelect",
            "signleSelect": {
                "beSelectValue": "2",
                "fillContent": ""
            }
        },
        {
            "subjectId": "1001640743801628001000000000001",
            "subjectType": "simpleFill",
            "simpleFill": {
                "inputContent": "无",
                "imgList": []
            }
        },
        {
            "subjectId": "1001640743816621000960000000001",
            "subjectType": "simpleFill",
            "simpleFill": {
                "inputContent": "无",
                "imgList": []
            }
        },
        {
            "subjectId": "1001640743859737000980000000001",
            "subjectType": "signleSelect",
            "signleSelect": {
                "beSelectValue": "1",
                "fillContent": ""
            }
        },
        {
            "subjectId": "1001640956029680001500000000001",
            "subjectType": "signleSelect",
            "signleSelect": {
                "beSelectValue": "flag1640956000651",
                "fillContent": ""
            }
        }
    ]
}