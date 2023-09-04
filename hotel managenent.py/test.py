import sqlite3

conn = sqlite3.connect("HOTEL MANAGEMENT.db")
cursor = conn.cursor()

l = [1, 2, 34, 5, 6]
for i in l:
    cursor.execute('''INSERT INTO Booking_table(number) 
                      VALUES(?,?)''', (i,))
    conn.commit()
