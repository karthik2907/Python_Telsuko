import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="2907",database="College")
data=mydb.cursor()

data.execute("select * from student")
result=data.fetchall()
re2=data.fetchmany(3)
#data=mycursor.execute("")

for i in re2:
    print(i)