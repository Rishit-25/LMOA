import sqlite3



def Book_table():
    conn = sqlite3.connect("ooks.db")
    cursor = conn.cursor()
        
    cursor.execute('''
                    CREATE TABLE ook_tale (
                        title text,
                        isn text
                       
                         )
                ''')
 
Book_table()