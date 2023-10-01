import sqlite3
import datetime




def advance_booking(name , email , adults , number , room_type , preference , special_preference , checkin_date , checkout_date ):
    
    conn = sqlite3.connect("HOTEL MANAGEMENT.db")
    cursor = conn.cursor()

    start_date = datetime.datetime.strptime(checkin_date, '%d-%m-%Y')
    end_date = datetime.datetime.strptime(checkout_date, '%d-%m-%Y')
    dates_reserved = []
    current_date = start_date

    while current_date <= end_date:
        dates_reserved.append(current_date.strftime('%d-%m-%Y'))
        current_date += datetime.timedelta(days=1)
    print("dates reserved = " , dates_reserved)

    dates_reserved_str =""

    for f in dates_reserved:
        dates_reserved_str = dates_reserved_str + f + " , "

            
    cursor.execute("SELECT * FROM Room_table")
    r= cursor.fetchall()
    print("room_table= " , r ) 

    
    
    i=0
    while i<=(len(r) - 1):
        #Selecting the row of the room no trying to be booked
        
        #
        print(r[i][2])
        if r[i][1] == room_type and r[i][2] == preference :

            cursor.execute(''' SELECT reserved_dates FROM Room_table WHERE Room_no = ?''' , (r[i][0] ,))
            c= cursor.fetchall()
            print("reserved dates from the rrom table = " , c )
            g=0
            for k in dates_reserved:
                if k in  c[0][0] :
                    i=i+1
                    break
                
                else:
                    g=1
                    
            # Finding the reserved dates of all the days the room has been booked
            if g == 1 :
            
                    x = c[0][0]
                    print(x)
                    y=x

                    for h in dates_reserved:
                        print(h)
                        y = y + h +  " , " 
                    print("y=" , y)


                    cursor.execute('''INSERT INTO  Booking_table(Room_no , Room_type , name , email , number , adults , preference , reserved_dates ) 
                           VALUES(?,?,?,?,?,?,?,?)  ''' , (  r[i][0] ,r[i][1] , name , email , number , adults , preference, dates_reserved_str ))

            #Inserting values in the mother table
                    
                    cursor.execute('''INSERT INTO  Mother_table(name , phone_no , email_id ,adults, Room_type , Room_no ,check_in , check_out ,reserved_dates, Amount_payable ) 
                           VALUES(?,?,?,?,?,?,?,?,?,?)  ''' , ( name, number , email , adults , r[i][1] , r[i][0] , checkin_date , checkout_date, dates_reserved_str ,  0  ))
                    
            #Inserting dates into room table
                    cursor.execute('''UPDATE Room_table SET reserved_dates = ? WHERE Room_no = ?''',  ( y, r[i][0] ))


                    conn.commit()
                    break

                

        
       
        
        else:
            print(i)
            i=i+1

advance_booking( name = "Rishit Aggarwal" , email = "2445@gmail.com" , adults = 3  , number = 647643 , room_type = "standard room", preference ="Smoking rooms",special_preference="nil" , checkin_date = "22-06-2023" , checkout_date = "26-06-2023")
        
        

