import sqlite3

conn = sqlite3.connect("ooks.d")
cursor = conn.cursor()

cursor.execute(
            '''SELECT * FROM ook_tales
'''
)

r= cursor.fetchall()

for i in r:
    print(r)