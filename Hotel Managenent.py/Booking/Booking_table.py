import sqlite3

def Booking_table():
    conn = sqlite3.connect("HOTEL MANAGEMENT.db")
    cursor = conn.cursor()
        
    cursor.execute('''
                    CREATE TABLE Booking_table (
                        booking_id INTEGER PRIMARY KEY ,
                        Room_no  integer  ,
                        Room_type text,
                        name text,
                        email text,
                        number integer,
                        adults integer,
                        preference text ,
                        gym     text,
                        mini_bar    text,
                        extra_bed text,
                        reserved_dates text
                       
                         )
                ''')
 
Booking_table()