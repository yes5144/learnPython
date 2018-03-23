#!/usr/bin/env python
# coding: utf8
# for python3.6

input = int(input('input a number: '))
for i in range(input):
    for j in range(i):
        print('*',end='.')  # end='.' 默认是换行
    print('\n')