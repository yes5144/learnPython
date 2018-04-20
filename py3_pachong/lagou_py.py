#!/usr/bin/env python
# coding: utf8
# python3
# author: channel
# about owner: https://www.cnblogs.com/QI1125/p/7577364.html

import requests
import xlwt
import time
import random

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36",
    "Referer":"https://www.lagou.com/jobs/list_Python?city=%E4%B8%8A%E6%B5%B7&cl=false&fromSearch=true&labelWords=&suginput=",
    "Cookie":"user_trace_token=20170914221143-a2fea78f-9956-11e7-9289-525400f775ce; LGUID=20170914221143-a2feae80-9956-11e7-9289-525400f775ce; _ga=GA1.2.1611186142.1505398301; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1524226506; LGSID=20180420201508-774dbd4b-4494-11e8-8f25-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; _gid=GA1.2.830756976.1524226506; index_location_city=%E4%B8%8A%E6%B5%B7; LGRID=20180420202439-cbb47f2f-4495-11e8-8f28-525400f775ce; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1524227155; _gat=1"
}

def getJobList(page):
    data = {
        'first':'false',
        'pn':page,
        'kd':'运维'
    }
    res = requests.post(
        'https://www.lagou.com/jobs/positionAjax.json?px=default&city=%E4%B8%8A%E6%B5%B7&needAddtionalResult=false',
        data=data,
        headers=headers,
    )
    result = res.json()
    jobs = result['content']['positionResult']['result']
    return jobs

# pa=getJobList(1)
# print(pa)

excelTabel= xlwt.Workbook()#创建excel对象
sheet1=excelTabel.add_sheet('lagou',cell_overwrite_ok=True)
sheet1.write(0,0,'公司名')#公司名
sheet1.write(0,1,'城市')#城市
sheet1.write(0,2,'地区')#地区
sheet1.write(0,3,'全职/兼职')#全职/兼职
sheet1.write(0,4,'薪资')#薪资
sheet1.write(0,5,'职位')#职位
sheet1.write(0,6,'工作年限')#工作年限
sheet1.write(0,7,'公司规模')#公司规模
sheet1.write(0,8,'学历')#学历

n=1
for page in range(1,4):
    time.sleep(random.randrange(1,7))
    for job in getJobList(page=page):
        sheet1.write(n, 0, job['companyFullName'])  # 公司名
        sheet1.write(n, 1, job['city'])  # 城市
        sheet1.write(n, 2, job['district'])  # 地区
        sheet1.write(n, 3, job['jobNature'])  # 全职/简直
        sheet1.write(n, 4, job['salary'])  # 薪资
        sheet1.write(n, 5, job['secondType'])  # 职位
        sheet1.write(n, 6, job['workYear'])  # 工作年限
        sheet1.write(n, 7, job['companySize'])  # 公司规模
        sheet1.write(n, 8, job['education'])  # 学历
        n += 1

excelTabel.save('lagou_运维.xlsx')