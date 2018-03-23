#!/usr/bin/env python
# coding: utf-8
# ps 可以查看进程的内存占用大小，写一个脚本计算一下所有进程所占用内存大小的和

import os
list = []
sum = 0
str1 = os.popen('ps aux','r').readlines()
for i in str1:
    str2 = i.split()
    new_rss = str2[5]
    list.append(new_rss)

for i in list[1:-1]:
    num = int(i)
    sum = sum + num
# print '%s:%s'%(list[0],sum)
print('%s:%s'%(list[0],sum))
# RSS: 330333