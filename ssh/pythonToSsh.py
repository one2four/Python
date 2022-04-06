'''
通过python paramiko模块，实现ssh连接linux后台
name: pythonToSsh.py 
date: 2021-06-23
'''
# -*- coding:utf-8 -*-

import paramiko

# 创建SSH对象
ssh = paramiko.SSHClient()
 
# 允许连接不在~/.ssh/known_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
 
# 连接服务器
ssh.connect(hostname="172.20.80.201", port=1022, username="administrator", password="lion@LL99")
# ssh.connect(hostname="172.20.88.112", port=22, username="root", password="123.com")


stdin, stdout, stderr = ssh.exec_command('interface show all')
# stdin.write("interface show all")
# print(stdout.read().decode())
# stdin, stdout, stderr = ssh.exec_command('iostat')

print(stderr.read().decode())

print(stdout.read().decode())
# stdin, stdout, stderr = ssh.exec_command("switchtodebug;n&9J~5#v")
# stdin, stdout, stderr = ssh.exec_command("mkdir 1")
# stdin.write("终端等待输入...\n")   # test.py文件有input()函数，如果不需要与终端交互，则不写这两行
# stdin.flush()
 
# 获取命令结果
# res, err = stdout.read(), stderr.read()
# result = res if res else err
# res = result.decode()
# res = result.decode("utf-8")
# res = result.decode(encoding="utf-8")
# print(res)
 
# 关闭服务器连接
ssh.close()

