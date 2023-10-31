import sqlite3

conn = sqlite3.connect("ooks.db")
cursor = conn.cursor()

cursor.execute(
            '''INSERT INTO  ook_tale VALUES ("UFUS" , "DJHSVHK")
'''
)

