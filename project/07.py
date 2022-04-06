# coding:utf-8
# L1=L 意思是将L1也指向L的内存地址,

# L1=L[:] 意思是, 复制L的内容并指向新的内存地址.

a = [1, 2, 3]
b = a
print(id(a))
print(id(b))
b = a[:]
print(id(a))
print(id(b))
print(b)
