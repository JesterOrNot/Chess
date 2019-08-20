import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="login"
)
mycursor = mydb.cursor()
username = input('What do you want your username to be').replace("'","")
password = input("What do you want your pass to be?: ").replace("''","")
sql = "INSERT INTO login(username,password,elo) VALUES (%s,%s,%s)"
val = (username, password, 1000)
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")