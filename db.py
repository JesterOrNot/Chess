import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="login_info"
)

mycursor = mydb.cursor()