import mysql.connector as mysql

def connect(db_name, password):

    try:

        return mysql.connect(host='localhost',
                           user='root',
                           password=password,
                           database=db_name)
    except Exception as e:
        print(e)

db = connect('hr','CISSYbravol@75')
cursor =db.cursor()
cursor.execute('select * from employees')
emp_records = cursor.fetchall()
print(emp_records)

db.close()