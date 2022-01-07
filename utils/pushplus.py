# -*- coding: UTF-8 -*-
# @Time    : 2022/1/1 17:05
# @Author  : Hui-Shao


import json
import traceback
import time
import logging
from datetime import datetime
import requests

logging.basicConfig(level=logging.INFO)


class PushPlus:
    @staticmethod
    def send(_token: str, _title: str, _content: str, _template: str = "html", _topic: str = "") -> bool:
        """
        :param _token: 用户令牌
        :param _title: 消息标题
        :param _content: 消息正文
        :param _template: 消息模板 可选 html txt markdown json
        :param _topic: 消息推送群组名称 用于一对多推送 不填则只推送给自己
        :return: bool
        """
        if len(_token) <= 5:
            return False
        url_send = "https://www.pushplus.plus/send"
        hea = {"Content-Type": "application/json"}
        data = {
            "token": _token,
            "title": _title,
            "content": _content,
            "template": _template,
        }
        if _topic:
            data.update({"topic": _topic})
        body = json.dumps(data).encode(encoding="utf-8")
        retry_n = 1
        while 1:
            if retry_n > 5:
                logging.error("\n达到最大重试次数, 退出")
                break
            try:
                res = requests.post(url=url_send, data=body, headers=hea)
            except requests.exceptions.SSLError:
                logging.error("SSL 错误, 2s后重试 -> SSLError: An SSL error occurred.")
                time.sleep(2)
            except requests.exceptions.ConnectTimeout:
                logging.error(
                    "建立连接超时, 5s后重试 -> ConnectTimeout: The request timed out while trying to connect to the remote server.")
                time.sleep(5)
            except requests.exceptions.ReadTimeout:
                logging.error(
                    "读取数据超时, 3s后重试 -> ReadTimeout: The server did not send any data in the allotted amount of time.")
                time.sleep(3)
            except requests.exceptions.ConnectionError:
                logging.error(f"{traceback.format_exc(3)}")
                logging.error("建立连接错误, 5s后重试")
                time.sleep(5)
            except requests.exceptions.RequestException:
                logging.error(f"{traceback.format_exc(3)}")
                logging.error("其他网络连接错误, 5s后重试")
                time.sleep(5)
            except KeyboardInterrupt:
                logging.warning("捕获到 KeyboardInterrupt, 退出")
                return False
            except Exception as e:
                sign = '=' * 60 + '\n'
                print(f'{sign}>>> Time: \t{datetime.now()}\n>>> "Detail": \t{e}')
                print(f'{sign}{traceback.format_exc()}{sign}')
            else:
                if res.text:
                    msg_back = json.loads(res.text)
                    if msg_back["code"] == 200:
                        print("[PushPlus] 请求推送消息成功！")
                        return True
                    else:
                        print("[PushPlus] 请求推送可能失败 返回值：%s" % (msg_back["msg"]))
                        return False
                else:
                    print("[PushPlus] 请求推送失败 res.text 为空!")
                    return False
            finally:
                retry_n += 1