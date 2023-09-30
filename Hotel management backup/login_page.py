import sqlite3

conn = sqlite3.connect("HOTEL MANAGEMENT.db")
cursor = conn.cursor()
    
cursor.execute('''
                CREATE TABLE  login_table (
                    email_id text ,
                    password  text PRIMARY KEY       )
            ''')
login_records = [ "rifjsn "  , "hdbij",
                "rifjsn "  ,"jhvedjhb" ,
                "rishitgmail.com" ,"ojhljh",
                "rishitgmail.com" ,"jnbgdfhb" ,
                "rishitgmail.com" , "gkjhgjb n",
                "rishitgmail.com" , "rlhgifb",
                "rishitgmail.com", " no"  
                ]
                

for i in range (0,len(login_records),2 ):
                                
    cursor.execute('''INSERT INTO login_table (email_id , password ) 
                VALUES(?,?) ''',(login_records[i],login_records[i+1]))

cursor.execute ('''SELECT * FROM login_table''')

r= cursor.fetchall()
print(r)



           

