import sqlite3
import  datetime

def billing( Room_no):
    conn = sqlite3.connect("HOTEL MANAGEMENT.db")
    cursor = conn.cursor()
        
    cursor.execute("SELECT * FROM Room_table")

    r= cursor.fetchall()
    print(r)
    
    i=0
    while i<=(len(r) - 1):
        if r[i][1] == room_type  and r[i][2] == 1:
            cursor.execute('''INSERT INTO  Booking_table(Room_no , Room_type ,name ,email,number , adults ) 
                           VALUES(?,?,?,?,?,?)  ''' , (  r[i][0] ,r[i][1] ,name,email,number,adults ))
            cursor.execute(''' UPDATE Room_table SET Avaibility = ? WHERE Room_no = ?



                            ''' ,(0,r[i][0]))
            conn.commit()
            print("kaam ho gya")
            return(r[i][0])
            break
        else:
            print(i)
            i=i+1