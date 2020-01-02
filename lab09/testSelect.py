import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="datarepresentation"
)
cursor = db.cursor()
sql="select * from patients where id = %s"
values = (1,)

cursor.execute(sql, values)
result = cursor.fetchall()

for x in result:
    print(x)