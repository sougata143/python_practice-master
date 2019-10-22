class first_class:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	
	def first_function(name):
		list = ["sougata", "rintu"]
		if 10>5:
			for x in list:
				print("for block "+x)
			print("if block "+name)	
	first_function("sougata")

	x = lambda a, b : a + b
	print(x(3, 19))

	def lambda_use(n):
		return lambda a : a * n
		
	multi = lambda_use(5)
	print(multi(11))

	def funtion_with_list(self):
		list = ["apple", 'samsung', 'nokia']
		for x in list:
			print('in for block '+x)
		if "apple" in list:
			print('in if block '+"apple is a brand")
		list.append("sony")
		print(list)
		list.remove("sony")
		print(list)
		print(self.name, self.age)
		myiter = iter(list)
		print(next(myiter))
		print(next(myiter))
		print(next(myiter))
		
	i = 1
	while i > 6:
		print(i)
		i+=1
		
myClass = first_class("Sougata", 26)
myClass.funtion_with_list()
print(myClass.i)
myClass.i = 10
print(myClass.i)