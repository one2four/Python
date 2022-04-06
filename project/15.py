#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-07-13 16:07:59
# @Author  : test  & (test@test.com)
# @Link    : https://github.com


score = int(input("input you score:"))

if score >= 90:
    grade = 'A'
elif score >= 60:
    grade = 'B'
else:
    grade = 'C'

print('%d belong %s' % (score, grade))
