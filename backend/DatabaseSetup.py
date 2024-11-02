import mysql.connector

input("Warning! This will DROP a database called 'cs2300project' and a user called cs2300backend. Hit Enter to continue")
rootPassword = input("Type in root password: ")
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=rootPassword
)

cursor = mydb.cursor()
f = open("SetupMysql.sql", encoding="utf-8")
for result in cursor.execute(f.read(), multi=True):
    print(result)
f.close()

print("Success!")