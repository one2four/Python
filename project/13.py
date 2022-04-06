#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-07-12 10:01:19
# @Author  : test  & (test@test.com)
# @Link    : https://github.com

for i in range(100, 10000):
    n = i // 100
    # print(n)
    l = i // 10 % 10
    # print(n)
    m = i % 10
    if i == n * n * n + l * l * l + m * m * m:
        print(i)
