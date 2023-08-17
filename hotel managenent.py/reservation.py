import sqlite3



conn = sqlite3.connect("HOTEL MANAGEMENT.db")
cursor = conn.cursor()
    
cursor.execute('''
                CREATE TABLE customers (
                    first_name  text,
                    second_name text,
                    phone_no integer,
                    email_id text,
                    reservations text,
                    check_in text,
                    check_out text        )
            ''')
insert_data=[ 

               "deeepam" , "fsd" , 41235235, "rifjsn " , " no " , "2nov" , " 5 dec" ,
               "deeepam" , "fsd" , 41235235, "rifjsn " , " no " , "2nov" , " 5 dec",
                "rishit", "aggarwal" , 672778896 , "rishitgmail.com"," no" , "2 november" , "5 november" ,
                "rishit", "aggarwal" , 672778896 , "rishitgmail.com"," no" , "2 november" , "5 november" ,
                "rishit", "aggarwal" , 672778896 , "rishitgmail.com"," no" , "2 november" , "5 november" ,
                "rishit", "aggarwal" , 672778896 , "rishitgmail.com"," no" , "2 november" , "5 november" ,
                "rishit", "aggarwal" , 672778896 , "rishitgmail.com"," no" , "2 november" , "5 november" ,
            
            ]
for i in range (0,len(insert_data),7 ):
                            
            cursor.execute('''INSERT INTO customers (first_name,second_name, phone_no , email_id , reservations , check_in , check_out ) 
                           VALUES(?,?,?,?,?,?,?) ''',(insert_data[i],insert_data[i+1],insert_data[i+2],insert_data[i+3],insert_data[i+4],insert_data[i+5],insert_data[i+6] )  )      
cursor.execute("SELECT * FROM customers")

r= cursor.fetchall()

print(r)