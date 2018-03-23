#!/usr/bin/env python
# coding: utf8
# this is for python2.7

import time
import os

new_time = time.strftime('%Y-%m-%d')
disk_status = os.popen('dir').readlines()

str1 = ''.join(disk_status)

#file() 函数用于创建一个 file 对象，它有一个别名叫 open()，更形象一些，它们是内置函数。参数是以字符串的形式传递的
f = open('disk' + new_time + '.log','w')

f.write('%s'%str1)
f.flush()
f.close()