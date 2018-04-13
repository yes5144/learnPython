#!/usr/bin/env python
# coding: utf8
# __Author__

from  bs4 import BeautifulSoup
from urllib import request
import os, sys
import time
import random
import re

if __name__ == '__main__':
    target_url = "http://www.biqukan.com/1_1094/"
    head = {}
    # head['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; W…) Gecko/20100101 Firefox/59.0'
    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
    target_req = request.Request(url=target_url, headers=head)
    target_response = request.urlopen(target_req)
    target_html = target_response.read().decode('gbk','ignore')
    listmain_soup = BeautifulSoup(target_html,'lxml')
    chapters = listmain_soup.find_all('div', class_ = 'listmain')
    download_soup = BeautifulSoup(str(chapters), 'lxml')
    begin_flag = False

    for child in download_soup.dl.children:
        if child != '\n':
            if child.string == u"《一念永恒》正文卷":
                begin_flag = True
            if begin_flag == True and child.a != None:
                download_url = 'http://www.biqukan.com' + child.a.get('href')
                download_name = child.string
                print(download_name + ' : ' + download_url)

