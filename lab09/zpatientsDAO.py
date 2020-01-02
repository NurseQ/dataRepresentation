import mysql.connector
class PatientsDAO:
    db=""
    def __init__(self):
        self.db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        
        database="datarepresentation"
        )
    def create(self, values):
        cursor = self.db.cursor()
        sql="insert into patients (name, diagnosis, DOB, doctor, gender) values (%s,%s,%s,%s,%s)"
        cursor.execute(sql, values)

        self.db.commit()
        return cursor.lastrowid
    def getAll(self):
        cursor = self.db.cursor()
        sql="select * from patients"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    def findByID(self, id):
        cursor = self.db.cursor()
        sql="select * from patients where id = %s"
        values = (id,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return result
    def update(self, values):
        cursor = self.db.cursor()
        sql="update patients set name= %s, diagnosis=%s, DOB=%s, doctor=%s, gender=%s  where id = %s"
        cursor.execute(sql, values)
        self.db.commit()
    def delete(self, id):
        cursor = self.db.cursor()
        sql="delete from patients where id = %s"
        values = (id,)
        cursor.execute(sql, values)
        self.db.commit()
        print("delete done")
patientsDAO = PatientsDAO()