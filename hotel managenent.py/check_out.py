import sqlite3


def check_out(Room_no):
    print(Room_no)
    conn = sqlite3.connect("HOTEL MANAGEMENT.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Booking_table WHERE Room_no = ?" , (Room_no,))


    cursor.execute(''' UPDATE Room_table SET Avaibility = ? WHERE Room_no = ?''' ,(1,Room_no))
    conn.commit()
    print("Room now Available")

check_out(201)

