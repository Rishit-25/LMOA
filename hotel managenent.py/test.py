import sqlite3

conn = sqlite3.connect("HOTEL MANAGEMENT.db")
cursor = conn.cursor()


cursor.execute(''' SELECT check_in,check_out FROM MOther_table WHERE Room_no = ?''' , (201,))

r=cursor.fetchall()
print(r)
