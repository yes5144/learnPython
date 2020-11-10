#!/usr/bin/env python
# coding: utf8

# Python监控CPU情况
#1、实现原理：通过SNMP协议获取系统信息，再进行相应的计算和格式化，最后输出结果
#2、特别注意：被监控的机器上需要支持snmp。yum install -y net-snmp*安装

# OID https://blog.csdn.net/buster2014/article/details/46925633

import os
def get_All_items(host,oid):
    sn1 = os.popen('snmpwalk -v 2c -c public ' + host + ' '+ oid + '|grep Raw |grep Cpu| grep -v Kernel').read().split('\n')[:-1]
    return sn1

def get_Date(host):
    items = get_All_items(host, '.1.3.6.1.4.1.2021.11')

    date = []
    rate = []
    cpu_total = 0
    # us = us + ni, sy = sy + irq + sirq
    for item in items:
        float_item = float(item.split(' ')[3])
        cpu_total += float_item
        if item == items[0]:
            date.append(float(item.split(' ')[3]) + float(item[1].split(' ')[3]))
        elif item == item[2]:
            date.append(float(item.split(' ')[3]) + float(item[5].split(' ')[3] + item[6].split(' ')[3]))
        else:
            date.append(float_item)

    # calculate cpu usage percentage
    for item in date:
        rate.append((item/cpu_total)*100)
    mean = ['%us','%ni','%id','%wa','%cpu_irq','%cpu_sIRQ']

    # calculate cpu usage percentage
    result = map(None, rate, mean)
    return result

if __name__ == '__main__':
    hosts = ['192.168.204.123','192.168.204.125']
    for host in hosts:
        print('='*8, + host + '='*8)
        result = get_All_items(host)
        print('Cpu(s)'),
        for i in range(5):
            print('%.2f%s' %(result[i][0], result[i][1]))
            print()
            print()

