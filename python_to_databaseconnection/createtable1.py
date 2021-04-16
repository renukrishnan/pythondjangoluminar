
import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    database="pythonfeb2",
    password="Password@123",
    auth_plugin="mysql_native_password"
)
cursor=db.cursor()
sql="create table staff(sid int,sname varchar(50),dept varchar(50),design varchar(50),salary int)"
cursor.execute(sql)
db.close()