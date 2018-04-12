#!/usr/bin/env python
# coding:utf8
# __Author__: channel

# 1/ 导入模块；2/获取网站源码；3/正则匹配；4/get
import urllib.request
import re
import random
import time

# http://www.wmpic.me/tupian/cute
header = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; W…) Gecko/20100101 Firefox/59.0"}
def gethtml():
    pages = urllib.request.urlopen(url="http://www.wmpic.me/tupian/cute")
    html = pages.read()
    html = html.decode('UTF-8')
    return html

def getimg(html):
    imgre = re.compile(r' src="(.*?)" class=')
    imglist = re.findall(imgre, html)
    x = 0
    for imgurl in imglist:
        print(imgurl)
        time.sleep(random.randint(2,5))
        # 下载, 文件夹d:\picture存在
        urllib.request.urlretrieve(imgurl,'D:\\picture\%s.jpg'% x)
        x += 1
        print('正在下载第 %s 张' %x)

html = gethtml()
print(getimg(html))
# print(gethtml())
