#!/usr/bin/env python
# coding: utf8
# this is for python2.7

import time
import os

new_time = time.strftime('%Y-%m-%d')
disk_status = os.popen('df -h').readlines()

str1 = ''.join(disk_status)
f = file('disk' + new_time + '.log','w')

f.write('%s'%str1)
f.flush()
f.close()