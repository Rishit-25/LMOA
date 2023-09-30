import sqlite3

conn = sqlite3.connect("HOTEL MANAGEMENT.db")
cursor = conn.cursor()

print(cursor.execute ('''SELECT * FROM login_table'''))

r= cursor.fetchall()

def login_check(email,password):
    global r
    for i in r :
        if i[0] == email and i[1] == password :
            return True
        else:
            return False 

