# coding:utf-8

def printme(str):
	print(str)
	return

# printme("test defhhhhh")
# printme("gogogogog")
#不定长参数
def printinfp(arg1,*vartuple):
	print("输出")
	print(arg1)
	for var in vartuple:
		print(var)
	return
# printinfp(10)
# printinfp(50,20,30,40)

#匿名函数
# count = lambda arg3,arg4:arg3+arg4
# print("相加后的值:",count(10,20))
# print("相加后的值:",count(30,40))

def count1(a1,a2):
	total = a1 + a2
		print("函数内:",total)
	return total

count1(10,20)



