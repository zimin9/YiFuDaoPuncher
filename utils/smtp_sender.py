# coding=utf-8
import smtplib
from email.mime.text import MIMEText


class ErrorEmail():
    def __init__(self, msg_from, pass_word, msg_to):
        '''
        发送邮件实体类
        :param msg_from: # 发送方邮箱
        :param pass_word: # 填入发送方邮箱的授权码
        :param msg_to: # 收件人邮箱
        '''
        self.msg_from = msg_from
        self.pass_word = pass_word
        self.msg_to = msg_to

    def theme_content(self, theme, content):
        '''
        构建邮件主题和内容
        :param theme:  主题
        :param content:  内容
        :return:
        '''
        msg = MIMEText(content)
        msg['Subject'] = theme
        msg['From'] = self.msg_from           # join 作用群发邮件
        msg['To'] = ''.join(self.msg_to)
        return msg

    def send_message(self, host, port, msg):
        '''
        发送邮件方法
        :param host: 第三方邮件host
        :param port:端口号
        :param msg:MIMETexe 对象
        :return:
        '''
        try:
            sm = smtplib.SMTP_SSL(host, port)
            sm.login(self.msg_from, self.pass_word)
            sm.sendmail(self.msg_from, self.msg_to, msg.as_string())
        except Exception as e:
            print(e)
        finally:
            sm.quit()