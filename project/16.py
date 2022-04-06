#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-07-13 16:11:43
# @Author  : test  & (test@test.com)
# @Link    : https://github.com


import datetime

if __name__ == '__main__':
    print(datetime.date.today().strftime('%d/%m/%Y'))

    Date1 = datetime.date(2018, 9, 9)

    print(Date1.strftime('%Y-%m-%d'))

    # 日期算数运算
    Date2 = Date1 + datetime.timedelta(days=3)

    print(Date2.strftime('%Y-%m-%d'))

    # Date3 = Date1 + datetime.timedelta
    # print(Date2.strftime('%Y-%m-%d'))
