#!/usr/bin/env python
# coding: utf8
# about owner: https://blog.csdn.net/qq_41673534/article/details/79324642

import requests
import pandas
import random
import time

city = "上海"
job = "python"
url = 'https://www.lagou.com/jobs/positionAjax.json?city='+city+'&needAddtionalResult=false'
header = {
    "Host":"www.lagou.com",
    "Origin":"https://www.lagou.com",
    "Pragma":"no-cache",
    "Referer":"https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36",
}

for num in range(1,5):
    time.sleep(random.randint(1,3))

    flag = 'true'
    if num!=1:
        flag='false'
    form = {
        'first':flag,
        'kd':job,
        'pn':str(num)
    }
    html = requests.post(url=url, data=form, headers=header)
    result = html.json()
    print("***********" + str(num) + "***********")
    data = result['content']['positionResult']['result']
    print(data)
    table = pandas.DataFrame(data)
    table.to_csv(r'lagoupython.csv', header = False, index=False, mode='a+')