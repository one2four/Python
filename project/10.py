#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-07-09 11:25:28
# @Author  : 124 (${email})
# @Link    : ${link}
# @Version : $Id$

import time

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
time.sleep(5)
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
