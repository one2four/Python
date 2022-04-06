# coding:utf-8

from ping3 import ping

second = ping('www.baidu.com')
unkonw = ping('123.1.2.3')
print(unkonw)

print('it took {} second'.format(second))
