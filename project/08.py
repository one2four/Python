#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-07-08 16:21:19
# @Author  : 124 (${email})
# @Link    : ${link}
# @Version : $Id$


for i in range(1, 10):
    print()
    for j in range(1, i + 1):
        print("%d*%d=%d" % (i, j, i * j), end=" ")
