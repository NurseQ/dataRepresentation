import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="datarepresentation"
)

mycursor = mydb.cursor()
sql="CREATE TABLE patients (id INT AUTO_INCREMENT PRIMARY KEY, name varchar(100), diagnosis varchar(100),DOB date, doctor varchar(100), gender enum('M','F'))"
mycursor.execute(sql)