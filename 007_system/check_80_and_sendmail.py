#!/usr/bin/env python
# coding: utf8
# 判断本机的80端口是否开启着，如果开启着什么都不做，
# 如果发现端口不存在，那么重启一下httpd服务，
# 并发邮件通知你自己。
# 脚本写好后，可以每一分钟执行一次，也可以写一个死循环的脚本，30s检测一次

# https://blog.csdn.net/offbeatmine/article/details/51790654
import os
import time
import sys
import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_simple_mail(warning):
    msg = MIMEText(warning)
    msg['Subject'] = 'python first mail'
    msg['From'] = 'root@localhost'
    try:
        smtp = smtplib.SMTP()
        smtp.connect(r'smtp.126.com')
        smtp.login('要发送的邮箱名','密码')
        smtp.sendmail('要发送的邮箱名',['要发送的邮箱名'], msg.as_string())
        smtp.close()
        print('邮件发送成功')
    except Exception as e:
        print (e)


while True:
    http_status = os.popen('netstat -tulnp |grep httpd','r').readlines()
    try:
        if http_status == []:
            os.system('service httpd start')
            time.sleep(5)
            new_http_status = os.popen('netstat -tulnp |grep httpd','r').readlines()
            str1 = ''.join(new_http_status)
            is_80 = str1.split()[3].split(':')[-1]
            if is_80 != '80':
                print('httpd 启动失败')
            else:
                print('httpd 启动成功成功')
                send_simple_mail(warning='This is a warning!!!')
        else:
            print('httpd 正常')
            time.sleep(5)
    except KeyboardInterrupt:
        sys.exit('\n')