import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    database="pythonfeb2",
    password="Password@123",
    auth_plugin="mysql_native_password"
)
cursor=db.cursor()
f=open("staff")# will read by each lines
for lines in f:
    data=lines.rstrip("\n").split(",")#will get list[102,renu,cse,lecturer,30000]
    sql="insert into staff(sid,sname,dept,design,salary)values(%s,%s,%s,%s,%s)"
    cursor.execute(sql,tuple(data))
    db.commit()
db.close()