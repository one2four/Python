#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-07-19 16:10:39
# @Author  : test  & (test@test.com)
# @Link    : https://github.com
# 计算圆的面积

def findArea(r):
    PI = 3.1415926535898
    return PI * (r * r)


print("面积:%.100f" % findArea(5))
