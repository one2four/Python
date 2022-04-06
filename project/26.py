#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-07-20 10:58:28
# @Author  : test  & (test@test.com)
# @Link    : https://github.com


# 阶乘
# n! = 1*2*3*4...*n

num = int(input('number:'))
foctorial = 1

if num < 0:
    print('error小于0')
elif num == 0:
    print('0的阶乘为1')
else:
    for i in range(1, num + 1):
        foctorial = foctorial * i
    print('%d 的阶乘为 %d' % (num, foctorial))
