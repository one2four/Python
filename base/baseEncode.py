# -*- coding:utf-8 -*-
# @Time    : 2022/3/29 11:00
# @Author  : unkown
# @File    : baseEncode.py
# @License : Unkown

import base64
import io

f1 = open('in.txt','r')
f2 = open('out.txt','w')
for line in f1:
    print(format(base64.b64encode(line.encode())))
# print(f1)
#
# base64.encode(f1,f2)
#
# f1.close()
# f2.close()
