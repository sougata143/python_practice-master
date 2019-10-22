import os

f = open("file.txt", "w")
f1 = open("file.txt", "r")
f2 = open("file.txt", "a")
f.write("Fuck The World")
print(f1.read())
for x in f1:
	print(x)

f.close()
f1.close()
f2.close()
os.remove("file.txt")