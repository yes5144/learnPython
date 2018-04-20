#!/usr/bin/env python
# coding: utf8
# python3.6
# about owner:https://blog.csdn.net/CSDN2497242041/article/details/77170746

from urllib import request
from bs4 import BeautifulSoup
import re
import time

url = "https://www.zhihu.com/question/22918070"
html = request.urlopen(url).read().decode('utf-8')
soup = BeautifulSoup(html,'html.parser')
# print(soup.prettify())
links = soup.find_all('img', "origin_image zh-lightbox-thumb",src=re.compile(r'.jpg$'))
# print(links)
path = r'D:\python36\mzitu'

for link in links:
    print(link.attrs['src'])
    request.urlretrieve(link.attrs['src'], path+'\%s.jpg'%time.time())