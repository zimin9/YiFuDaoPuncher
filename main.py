# -*- encoding:utf-8 -*-
from YiFuDao_Puncher import YiFuDao_Puncher
from default_data import *
from utils.dingding_bot import DingDingBot
from utils.smtp_sender import ErrorEmail
from utils.time_util import datetime_2string


if __name__ == '__main__':
    puncher = YiFuDao_Puncher()
    title = "奕辅导健康打卡通知：{}".format(puncher.puncher_status)
    text = """
            *** 奕辅导健康打卡通知 ***
            时间：{}
            打卡情况：{}
            """.format(datetime_2string(), puncher.puncher_status)

    if notify == "DingDing":
        notifier = DingDingBot(dingding_access_token,dingding_secret)
        notifier.set_msg(title,text)
        notifier.send()
    elif notify == "Mail":
        ee = ErrorEmail(mail_sender, mail_auth_code, mail_receiver)
        msg = ee.theme_content(title,text)
        ee.send_message(mail_smtp_link, mail_smtp_port, msg)
