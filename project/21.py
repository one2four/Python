#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-07-19 16:07:02
# @Author  : test  & (test@test.com)
# @Link    : https://github.com
# 计算素数

lower = int(input('lower:'))
upper = int(input('upper:'))

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
