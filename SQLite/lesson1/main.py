import sqlite3
#
# name =  input("Name? ")
# position = input("Position? ")
connection = sqlite3.connect('hr.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Employees 
              (Emp_ID INT, Name TEXT, Position TEXT)''')

employees = [(1, 'Elsad', 'Instructor'),
             (2, 'Ronald', 'Developer'),
             (3, 'e','e')]

cursor.execute('''INSERT INTO Employees VALUES (?, ?, ?)''',employees)

connection.commit()
connection.close()