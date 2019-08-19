import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="login"
)

mycursor = mydb.cursor()


mycursor.execute("""CREATE TABLE login (
    id INT AUTO_INCREMENT PRIMARY KEY,
    login_username VARCHAR(255) NOT NULL,
    login_password VARCHAR(255) NOT NULL
    )
""")