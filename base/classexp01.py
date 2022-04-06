# conding:utf-8
class person:
	def __init__(self,name,gen,age,fig):
		self.name = name
		self.gen = gen
		self.age =  age
		self.fig = fig

	def grassland(self):
		self.fig = self.fig - 200

	def parctice(self):
		self.fig = self.fig + 200

	def  incest(self):
		self.fig = self.fig - 500

	def detail(self):
		temp = "name:%s; gen:%s; age:%s; fig:%s" %(self.name,self.gen,self.age,self.fig)
		print(temp)

cang = person('cang','w',18,1000)
dong = person('dong','m',20,1800)
bo = person('bo','w',19,2500)

cang.incest()
dong.parctice()
bo.grassland()

cang.detail()
dong.detail()
bo.detail()

cang.incest()
dong.incest()
bo.parctice()


cang.detail()
dong.detail()
bo.detail()