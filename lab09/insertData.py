import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="datarepresentation"
)
cursor = db.cursor()
sql="insert into patients (name, diagnosis, DOB, doctor, gender) values (%s,%s,%s,%s,%s)"
values = ("Mary","Heart Burn", '1995-04-05', "Dr. Murray", "F" )

cursor.execute(sql, values)

db.commit()
print("1 record inserted, ID:", cursor.lastrowid)