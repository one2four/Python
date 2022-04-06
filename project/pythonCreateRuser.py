# -*- coding:utf-8 -*-
# @Time    : 2021/11/24 14:23
# @Author  : unkown
# @File    : pythonCreateRuser.py
# @License : Unkown

for i in range(30, 150):
    print("User-Name=t%d\n"
          "Cleartext-Password=1\n"
          "Calling-Station-Id=0000-2222-00%d\n"
          "Nas-IP-Address=172.20.80.1\n"
          "Nas-Port-Id=0/0/%d\n"
          "EAP-Code=Response\n"
          "EAP-Id=%d\n"
          "EAP-Type-Identity=t%d\n"
          "Message-Authenticator=0x00\n" %(i,i,i,i,i))
