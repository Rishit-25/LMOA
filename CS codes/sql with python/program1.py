import sqlite3

conn = sqlite3.connect("ooks.db")
cursor = conn.cursor()

cursor.execute(
            '''SELECT * FROM ook_tale
'''
)

r= cursor.fetchall()

for i in r:
    print(r)