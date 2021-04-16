import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    database="pythonfeb2",
    password="Password@123",
    auth_plugin="mysql_native_password"
)
cursor=db.cursor()
#sql="create table staff(sid int,sname varchar(50),dept varchar(50),design varchar(50),salary int)"
sql="insert into staff(sid,sname,dept,design,salary)values(100,'ajay','CSE','lecturer',25000)"
try:
    cursor.execute(sql)
    db.commit()
except Exception as e:
    print(e.args)
    db.rollback()
finally:
    db.close()