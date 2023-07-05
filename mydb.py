# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Goldbling2004'
)


cursor = dataBase.cursor()

# create a database
sql = "CREATE DATABASE mycrm"


cursor.execute(sql)

print("Database created successfully")