import sqlite3



def Mother_table():
    conn = sqlite3.connect("HOTEL MANAGEMENT.db")
    cursor = conn.cursor()
        
    cursor.execute('''
                    CREATE TABLE Mother_table (
                        name  text,
                        phone_no integer,
                        email_id text,
                        Room_no integer,
                        Room_type  text,
                        check_in text,
                        check_out text,
                        advance_booking text,  
                        Paid_Amount integer      )
                ''')

Mother_table()
    

  