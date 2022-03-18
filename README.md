# 奕辅导健康打卡脚本

本项目为Python脚本所写，适合用于有python运行环境的机器。不熟悉python的小伙伴可以看一下基于云函数的打卡脚本，部署更加方便快捷：

https://github.com/Chorer/YiFuDaoChecker-cloudFunction

基于圈X，且功能更多的脚本：

https://github.com/uiolee/NanFuDao



### 📌 快速上手

#### 1、使用抓包软件获取自己奕辅导小程序账号的access_token



#### 2、打开 `default_data.py`，填写相关配置信息

**2.1 配置打卡信息：**

```python
# 打卡的accessToken
accessToken = "tW4ATw/+dOxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxmJuyfpfYcAsuSnOn2chlDaLo8r+hMVBStA1O2JxotiyzEJBxxxxxxxxxxxxxxxxxTxV/ZQ2kjxfYjqsaw/M9AiZ2Glqg=="

# 打卡数据
punch_in_data = {
    ……
}
```

将第一步抓取到的access_token粘贴到第一个变量中。

💚**2022年1月10日更新：**

打卡信息现在可以使用 `punch_in_data_generator.py` 脚本进行抓取。使用方法：

1. 现在手机上正常打卡
2. 使用 python 运行 `punch_in_data_generator.py` 脚本
3. 将生成的 `punch_in_data.json` 文件中的数据全部复制到 `default_data.py` 中对应的 `punch_in_data` 变量



**2.2 配置通知提醒**

```python
notify = "DingDing"
```

notify目前可以填入DingDing / Mail / PushPlus / None，分别对应钉钉机器人推送、邮件推送、PushPlus推送与无推送。

设置钉钉机器人时，需要把钉钉机器人的access_token与secret填入下方对应的变量：

```python
## 钉钉机器人配置:
# access_token
dingding_access_token = "9b121xxxxxxxxxxxxxx508be80a2097xxxxxxxxx"
# secret
dingding_secret = "SEC324xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx260243754ac07708ebb905"
```

设置邮箱提醒时，需要把发件人、授权码、收件人、smtp地址与端口填入下方对应的变量：

```python
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
```

以下是PushPlus推送的设置：

```python
# PushPlus配置：
# token
pushplus_token = "2exxxxxxxxxxxxxxxxxxxx0fcb0cbed3"
```



#### 3、配置python运行环境

```cmd
pip install requests
```



#### 4、配置定时执行脚本

**💻 Linux系列系统**

使用cron定时执行，下面是每小时（的第一分钟时）执行一次打卡程序的例子：

```
1 * * * * python3 /home/xxxx/main.py
```

cron的具体使用教程可以参考这篇文章：[Linux crontab 命令 ｜ 菜鸟教程](https://www.runoob.com/linux/linux-comm-crontab.html)

**💻 Windows系统**

使用系统的“定时任务设置”即可，可视化配置非常简单，参考文章：[window下设置定时任务及基本配置 ｜ cnblog](https://www.cnblogs.com/funnyzpc/p/11746439.html)



### 💬 反馈

出现bug或其他异常情况欢迎直接提issue。

有必要时附上脚本运行日志，日志文件名为`YiFuDaoPuncher.log`



### 📢 声明

1. 本项目仅供编程学习/个人使用，请遵守Apache-2.0 License开源项目授权协议。
2. 请在国家法律法规和校方相关原则下使用。
3. 开发者不对任何下载者和使用者的任何行为负责。



### 📆 相关计划

https://github.com/zimin9/YiFuDaoPuncher/milestones
