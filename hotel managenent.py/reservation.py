import sqlite3



def input_reservations():
        a=input("Enter the  name  :  " )
        b=int(input("phone number :  "))
        c=input("enteer your gmail : ")
        d=input("Enter teh chenck in date :  ")
        e=input("Enetr the checkout date :  ")
        insert_data.append(a)
        insert_data.append(b)
        insert_data.append(c)
        insert_data.append(d)
        insert_data.append(e)
        
def reservations():

    conn = sqlite3.connect("HOTEL MANAGEMENT.db")
    cursor = conn.cursor()
        
    cursor.execute('''
                    CREATE TABLE reservation_customers (
                        first_name  text,
                        second_name text,
                        phone_no integer,
                        email_id text,
                        reservations text,
                        check_in text,
                        check_out text        )
                ''')
    
    insert_data=[]        


    for i in range (0,len(insert_data),7 ):
                                
                cursor.execute('''INSERT INTO reservation_customers (first_name,second_name, phone_no , email_id , reservations , check_in , check_out ) 
                            VALUES(?,?,?,?,?,?,?) ''',(insert_data[i],insert_data[i+1],insert_data[i+2],insert_data[i+3],insert_data[i+4],insert_data[i+5],insert_data[i+6] )  )      
    cursor.execute("SELECT * FROM customers")

    r= cursor.fetchall()

    print(r)




#_______________________________________________________________________________________________________________________________________________________________________________________________
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#_______________________________________________________________________________________________________________________________________________________________________________________________
#    
   
   
   
   
   
   def login_table(inputed_data):
    conn = sqlite3.connect("HOTEL MANAGEMENT.db")
    cursor = conn.cursor()
        
    cursor.execute('''
                    CREATE TABLE total_customers (
                        first_name  text,
                        second_name text,
                        phone_no integer,
                        email_id text,
                        reservations text,
                        check_in text,
                        check_out text        )
                ''')
       
    
 
 
 
 # ________________________________________________________________________________________________________________________________________________________________________________________________________________________________              
   
   
   
   
   
   
   
   
    def display():
                                ]
            for i in range (0,len(insert_data),7 ):
                                        
                        cursor.execute('''INSERT INTO total_customers (first_name,second_name, phone_no , email_id , reservations , check_in , check_out ) 
                                    VALUES(?,?,?,?,?,?,?) ''',(insert_data[i],insert_data[i+1],insert_data[i+2],insert_data[i+3],insert_data[i+4],insert_data[i+5],insert_data[i+6] )  )      
            cursor.execute("SELECT * FROM total_customers")

            r= cursor.fetchall()

            print(r)

