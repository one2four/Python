#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-07-08 16:29:58
# @Author  : 124 (${email})
# @Link    : ${link}
# @Version : $Id$
import time

myD = {1: 'a', 2: 'b'}
for key, value in dict.items(myD):
    print(key, value)
    time.sleep(1)
