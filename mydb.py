import mysql.connector

database = mysql.connector.connect(
   host = '127.0.0.1',
   user = 'root',
   passwd = 'Your-mysql-db-password'
)

cursor_object = database.cursor()

cursor_object.execute("CREATE DATABASE dcrm")

print("dcrm database created!")