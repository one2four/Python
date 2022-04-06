#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-07-20 10:18:27
# @Author  : test  & (test@test.com)
# @Link    : https://github.com


# 通过海伦公式计算三角形面积
# 已知三家行三条边长，计算三角形面积

a = float(input('a:'))
b = float(input('b:'))
c = float(input('c:'))

s = (a + b + c) / 2

area = (s * (s - a) * (s - b) * (s - c))**0.5

print('area %.100f' % area)
