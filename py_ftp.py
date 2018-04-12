#!/usr/bin/env python
# coding: utf8
# this is python 3.6

# import paramiko
#
# t = paramiko.Transport((hostname, port))
# t.connect(username=username, password=password)
# sftp = paramiko.SFTPClient.from_transport(t)
# remotepath = '/tmp/test.txt'
# localspath = '/test.txt'
#
# # get是获取函数，put是上传函数
# sftp.get(localspath, remotepath)
# t.close()

import paramiko
import datetime
import os,sys

def getFileFromServer(ip, remote_dir, local_dir):
    try:
        t = paramiko.Transport((ip, 22))
        t.connect(username='login_user', password='passwd')
        sftp = paramiko.SFTPClient.from_transport(t)

        files = sftp.listdir(remote_dir)
        for f in files:
            print('')
            print("*"*15)
            print('begin to download file from %s %s'%(ip, datetime.datetime.now()))
            print('Download file:', os.path.join(remote_dir))
            sftp.get(os.path.join(remote_dir,f), os.path.join(local_dir, f))

            print('Download file success %s' % datetime.datetime.now())
            print('')
            print('*'*15)
        t.close()
    except Exception:
        print('connect error')

