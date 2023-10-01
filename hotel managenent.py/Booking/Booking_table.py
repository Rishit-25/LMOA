import sqlite3

def Booking_table():
    conn = sqlite3.connect("HOTEL MANAGEMENT.db")
    cursor = conn.cursor()
        
    cursor.execute('''
                    CREATE TABLE Booking_table (
                        Room_no  integer  ,
                        Room_type text,
                        name text,
                        email text,
                        number integer,
                        adults integer,
                        preference text , 
                        reserved_dates 
                       
                         )
                ''')
 
Booking_table()