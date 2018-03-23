#!/usr/bin/env python
# coding:utf8
#  this is python3.6

import os,sys
import subprocess

# 获取执行状态返回值
os.system('netstat -tnlp | grep http')

if (os.system('netstat -tnlp |grep http') == 0):
    print('process http exists')

# 获取执行结果os.popen，
# 更为强大的是subprocess.Popens
if (os.popen('netstat -ntlp |grep http').read() !=''):
    print('process http exists')

print(os.system('dir'))
print(os.system('ls'))

subprocess.getstatusoutput('ls /bin/ls')

subprocess.getstatusoutput('cat /bin/junk')

subprocess.getstatusoutput('/bin/junk')

