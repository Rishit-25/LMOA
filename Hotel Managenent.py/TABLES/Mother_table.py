import sqlite3



def Mother_table():
    conn = sqlite3.connect("HOTEL MANAGEMENT 1.db")
    cursor = conn.cursor()
        
    cursor.execute('''
                    CREATE TABLE Mother_table (
                        name  text,
                        booking_id integer PRIMARY KEY,
                        phone_no integer,
                        email_id text,
                        adults integer,
                        Room_no integer,
                        Room_type  text,
                        gym     text,
                        mini_bar    text,
                        extra_bed text,
                        check_in text,
                        check_out text,
                        reserved_dates text,  
                        Amount_payable integer      )
                ''')

Mother_table()
    

  