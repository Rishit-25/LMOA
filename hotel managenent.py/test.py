import sqlite3
conn = sqlite3.connect("HOTEL MANAGEMENT.db")
cursor = conn.cursor()


cursor.execute(''' SELECT * FROM MOther_table WHERE Room_no = ? And name = ? ''' , (125,"Rishit Aggarwal" )) 
r=cursor.fetchall()
print(r)