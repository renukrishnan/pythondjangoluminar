#mysql-connector
#step1 --> import mysql module
import mysql.connector
#step -->  establish connection
db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Password@123",
    auth_plugin="mysql_native_password"
)
#step3 --> create cursor object# cursor object is usng to transport data from mysql to python and python to mysql
cursor=db.cursor()
#step4 --> execute sql queries
sql="select version()"
cursor.execute(sql)
data=cursor.fetchone()
print(data)
#step5--> close db connection