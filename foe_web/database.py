import mysql.connector as mysql

db = mysql.connect(
    host= 'localhost',
    user= 'root',
    passwd= '',
    database= 'foe'
)

sql = mysql

cursor = db.cursor()