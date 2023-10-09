import sqlite3
conn = sqlite3.connect("HOTEL MANAGEMENT.db")
cursor = conn.cursor()

cursor.execute(''' SELECT * FROM Mother_table WHERE  booking_id = ?  ''' , (6, )) 
r=cursor.fetchall()
print(r)