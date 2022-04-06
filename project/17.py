#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-07-13 16:59:07
# @Author  : test  & (test@test.com)
# @Link    : https://github.com


import string

s = input('input strings:\n')
letters = 0
space = 0
digit = 0
others = 0

for c in s:
    if c.isalpha():
        letters += 1
    elif c.isspace():
        space += 1
    elif c.isdigit():
        digit += 1
    else:
        others += 1
print('char = %d ,space = %d,digit = %d,others = %d' %
      (letters, space, digit, others))
