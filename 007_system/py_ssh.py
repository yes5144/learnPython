#!/usr/bin/env python
# coding: utf8
# python3.6

import paramiko

# create ssh class
ssh = paramiko.SSHClient()

# know_hosts
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# ssh 192.168.0.131
ssh.connect(hostname='192.168.0.131', port=22, username='root', password='channel2@')

# exec command
stdin, stdout, stderr = ssh.exec_command('df')

# get result
result = stdout.read()
print('this is df :', result)

# close ssh
ssh.close()

# coding: utf8

import paramiko

username = 'root'
password = 'Aliun32233'
hostname = '192.168.0.23'
port = 22

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname,port, username, password)

stdin, stdout, stderr = ssh.exec_command('uptime')
print('result:',stdout.readlines())
ssh.close()


