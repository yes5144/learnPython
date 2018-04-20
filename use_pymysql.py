#!/usr/bin/env python
# coding: utf8
# author channel
#

import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    port = 3306,
    user = 'root',
    password = '123123',
    db = 'mysql'
)

cursor = conn.cursor()
cursor.execute('select version()')
row = cursor.fetchone()
print('Mysql server version:', row[0])
cursor.close()
conn.close()