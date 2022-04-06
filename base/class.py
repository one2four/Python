# conding:utf-8

class foo():
	#构造函数
	def __init__(self,name,age):
		self.name = name
		self.age = age

	def detail(self):
		print(self.name)
		print(self.age)

obj1 = foo('change',18)
obj1.detail()
# print(obj1.name)
# print(obj1.age)
obj2 = foo('python',100)
obj2.detail()

# print(obj2.name)
# print(obj2.age)

