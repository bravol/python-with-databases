import sqlite3
import csv


connection = sqlite3.connect('data.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Population
             (City TEXT, Country TEXT, Population INT)''')

# file = open('population_data.csv')
# city_data = csv.reader(file)
# city_data.__next__()
# cursor.executemany('''INSERT INTO Population VALUES (?, ?, ?)''', city_data)
#

results =  cursor.execute('''SELECT * FROM Population''')
# print(cursor.fetchall())

for row in results:
    print(row)

connection.commit()
connection.close()