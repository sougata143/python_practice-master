import mysql.connector

mydb = mysql.connector.connect(
	host = "localhost",
	user = "",
	passwd = "",
	database = "pydatabase"
)

mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)
mycursor.execute("CREATE DATABASE pydatabase")