#import prac as pr
import datetime as dt
import json
import camelcase

class User:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	
	def class_method(self):
		print("Hello World from "+self.name)
	
p1 = User("Sougata", 26)
p1.class_method()
#p2 = pr.first_class("Sougata", 26)
#p2.funtion_with_list()
d = dt.datetime.now()
print(d.year)
print(d.month)
print(d.day)
print(d.date)
print(d.time)
print(d.strftime("%A"))
print(d.strftime("%x"))

j = {
	"name":"Sougata",
	 "Age":26, 
	 "Address":"Kolkata", 
	 "Email":"sroy@slscomptech.com"}
#js = json.loads(j)
#print(j["name"])
#json.dumps(js, indent=4, separators=(". ", " = "))
#print(z)

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])
df = json.dumps(j, indent=4, separators=(". ", " = "), sort_keys=True)
print(df)

c = camelcase.CamelCase()
txt = "hello world"
print(c.hump(txt))

try:
	print(jkio)
except NameError:
	print("Name Error Occured")
except:
	print("Other Error")
else:
	print("inside else")
finally:
	#x = 8
	#print(x)
	print("inside finally")
