import sqlite3
import datetime




def booking( name,email,adults,number,room_type,checkin_date):
    
    conn = sqlite3.connect("HOTEL MANAGEMENT.db")
    cursor = conn.cursor()
    start_date = datetime.datetime.strptime(start_date_str, '%d-%m-%Y')
    end_date = datetime.datetime.strptime(end_date_str, '%d-%m-%Y')
    
    current_date = start_date
    
    while current_date <= end_date:
        print(current_date.strftime('%Y-%m-%d'))
        current_date += datetime.timedelta(days=1) 
        
    cursor.execute("SELECT * FROM Room_table")

    r= cursor.fetchall()
    print(r)
    
    i=0
    while i<=(len(r) - 1):
        if r[i][1] == room_type  and preference =  :
            #Inserting values in the booking table
            cursor.execute('''INSERT INTO  Booking_table(Room_no , Room_type , name , email , number , adults , DATE) 
                           VALUES(?,?,?,?,?,?,?)  ''' , (  r[i][0] ,r[i][1] , name , email , number , adults , checkin_date ))
            
            
            #Inserting values in the mother table
            cursor.execute('''INSERT INTO  Mother_table(name,phone_no , email_id , Room_type , Room_no ,check_in , check_out , Paid_Amount ) 
                           VALUES(?,?,?,?,?,?,?,?)  ''' , ( name, number,email,r[i][1],r[i][0] , checkin_date , "--", 0  ))
            
            conn.commit()
            print("kaam ho gya")
            return(r[i][0])
        
        else:
            print(i)
            i=i+1

booking("Rishit Aggarwal" , "2445@gmail.com" , 3 , 647643, "standard room","22/06/23")
        
        

