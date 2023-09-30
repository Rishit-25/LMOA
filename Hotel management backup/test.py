cursor.execute("SELECT * FROM Booking_table WHERE Room_no = ?" , (r[i][0]))
        b= cursor.fetchall()
        print(b)