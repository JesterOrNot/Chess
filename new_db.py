import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE login_info")