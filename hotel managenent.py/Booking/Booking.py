import sqlite3
import datetime



def booking( name,email,adults,number,room_type,Check_in,check_out):
    
    
    
    conn = sqlite3.connect("HOTEL MANAGEMENT.db")
    cursor = conn.cursor()

    #Finding out the dates the room is being tried to be booked for
    start_date = datetime.datetime.strptime(checkin_date, '%d-%m-%Y')
    end_date = datetime.datetime.strptime(checkout_date, '%d-%m-%Y')
    dates_reserved = []
    current_date = start_date

    while current_date <= end_date:
        dates_reserved.append(current_date.strftime('%Y-%m-%d'))
        current_date += datetime.timedelta(days=1)
    print(dates_reserved)
        
    cursor.execute("SELECT * FROM Room_table")

    r= cursor.fetchall()
    print(r)
    
    i=0
    while i<=(len(r) - 1):
        if r[i][1] == room_type  and r[i][2] == 1:
            #Inserting values in the booking table
            cursor.execute('''INSERT INTO  Booking_table(Room_no , Room_type , name , email , number , adults , Advanced_booking , reseved_dates) 
                           VALUES(?,?,?,?,?,?,?)  ''' , (  r[i][0] ,r[i][1] , name , email , number , adults , Check_in))
            
            #Updating the Avaibility of the room 
            cursor.execute(''' UPDATE Room_table SET Avaibility = ? WHERE Room_no = ? ''' ,(0,r[i][0]))

            #Inserting values in the mother table
            cursor.execute('''INSERT INTO  Mother_table(name,phone_no , email_id , Room_type , Room_no ,check_in , check_out , Paid_Amount ) 
                           VALUES(?,?,?,?,?,?,?,?)  ''' , ( name, number,email,r[i][1],r[i][0] , date , "--", 0  ))
            
            conn.commit()
            print("kaam ho gya")
            return(r[i][0])
            break
        else:
            print(i)
            i=i+1

booking("Rishit Aggarwal" , "2445@gmail.com" , 3 , 647643, "standard room")
        
        
