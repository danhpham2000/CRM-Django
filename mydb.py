import mysql.connector


database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'David2022!pcd'
)

# prepare cursor object
cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE crm")

print("ALL DONE!")