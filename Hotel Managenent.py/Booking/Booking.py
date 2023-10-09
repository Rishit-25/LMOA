import sqlite3
import datetime




def advance_booking( name , email , adults , number , room_type , preference , special_preference , checkin_date , checkout_date ):
    
    conn = sqlite3.connect("HOTEL MANAGEMENT.db")
    cursor = conn.cursor()

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
        #Selecting the row of the room no trying to be booked
        cursor.execute("SELECT * FROM Booking_table WHERE Room_no = ?" , (r[i][0]))
        b= cursor.fetchall()
        print(b)

        if r[i][1] == room_type  :
            cursor.execute(''' SELECT reserved_dates FROM Booking table WHERE Room_no = ?''' , (r[i][0]))
            c= cursor.fetchall()
            for k in dates_reserved:
                if k in  c[0] :
                    i=i+1
                break

        
        elif r[i][1] == room_type  and r[i][2] == 1:
            
            dates_reserved_str = "" 
            for j in dates_reserved:
                a= str(j)
                dates_reserved_str  =  dates_reserved_str + " , " + a
            #Inserting values in the booking table
            cursor.execute('''INSERT INTO  Booking_table(Room_no , Room_type , name , email , number , adults , Advance_booking , reserved_dates ) 
                           VALUES(?,?,?,?,?,?,?,?)  ''' , (  r[i][0] ,r[i][1] , name , email , number , adults , "yes", dates_reserved_str  ))

            #Inserting values in the mother table
            cursor.execute('''INSERT INTO  Mother_table(name , phone_no , email_id , Room_type , Room_no ,check_in , check_out ,advance_booking, Paid_Amount ) 
                           VALUES(?,?,?,?,?,?,?,?,?)  ''' , ( name, number,email,r[i][1],r[i][0] , checkin_date , checkout_date,"yes", 0  ))
            
            conn.commit()
            print("kaam ho gya")
            return(r[i][0])
        
        else:
            print(i)
            i=i+1

advance_booking("Rishit Aggarwal" , "2445@gmail.com" , 3 , 647643, "standard room","22-06-2023" , "26-06-2023")
        
        

