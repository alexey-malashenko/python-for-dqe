import sqlite3

sdd = sqlite3.connect('publication.db')
cursor = sdd.cursor()

cursor.execute('SELECT * From ad')
result = cursor.fetchall()
#     print(result)
print(result)