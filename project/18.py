#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-07-13 17:03:02
# @Author  : test  & (test@test.com)
# @Link    : https://github.com

from functools import reduce
Tn = 0
Sn = []
n = int(input('n= '))
a = int(input('a= '))

for count in range(n):
    Tn = Tn + a
    a = a * 10
    Sn.append(Tn)
    print(Tn)

Sn = reduce(lambda x, y: x + y, Sn)
print(Sn)
