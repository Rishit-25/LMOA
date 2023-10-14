import sqlite3
import datetime



def advance_booking(name , email , adults , number , room_type , preference , gym , mini_bar , extra_bed , checkin_date , checkout_date ):
    
    
    conn = sqlite3.connect("HOTEL MANAGEMENT.db")
    cursor = conn.cursor()

    # FINDIND THE NO OF DAYS THE ROOM IS TRYING TO BE BOOKED

    start_date = datetime.datetime.strptime(checkin_date, '%d-%m-%Y')
    end_date = datetime.datetime.strptime(checkout_date, '%d-%m-%Y')
    dates_reserved = []
    current_date = start_date
     
    while current_date <= end_date:
        dates_reserved.append(current_date.strftime('%d-%m-%Y'))
        current_date += datetime.timedelta(days=1)
    print("dates reserved = " , dates_reserved)

    # CONVERTING THE FORMAT OF THE DATES TO STRING
    dates_reserved_str =""

    for f in dates_reserved:
        dates_reserved_str = dates_reserved_str + f + " , "

            
    cursor.execute("SELECT * FROM Room_table")
    r= cursor.fetchall()
    print("room_table= " , r ) 

    
    # BOOKING THE ROOM 
    i=0
    while i<=(len(r) - 1):

        #Selecting the row of the room no trying to be booked
        print(r[i][1])
        print(r[i][2])
       
        
        if r[i][1] == room_type and r[i][2] == preference :

            cursor.execute(''' SELECT reserved_dates FROM Room_table WHERE Room_no = ?''' , (r[i][0] ,))
            c= cursor.fetchall()
            print("reserved dates from the rrom table = " , c )

            g=0

            # CHECKING IF THE RROM HAS BEEN RESERVED BEFORE 
            for k in dates_reserved:
                print(k)
                if k in  c[0][0] :
                    i=i+1
                    g=1
                    break
                
                
                    
            # Finding the reserved dates of all the days the room has been booked
            if g == 0 :
            
                x = c[0][0]
                print(x)
                y=x
                print(dates_reserved)
                for h in dates_reserved:
                    print(h)
                    y = y + h +  " , " 
                    print("y=" , y)
            # INSERTING DATA INTO BOOKIING TABLE

                cursor.execute('''INSERT INTO  Booking_table(Room_no , Room_type , name , email , number , adults , preference  ,gym , mini_bar , extra_bed , reserved_dates ) 
                        VALUES(?,?,?,?,?,?,?,?,?,?,?)  ''' , (  r[i][0] ,r[i][1] , name , email , number , adults , preference,  gym , mini_bar , extra_bed ,  dates_reserved_str ))

        #Inserting values in the mother table
                
                cursor.execute('''INSERT INTO  Mother_table(name , phone_no , email_id ,adults, Room_type , Room_no , gym , mini_bar , extra_bed ,check_in , check_out ,reserved_dates, Amount_payable ) 
                        VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)  ''' , ( name, number , email , adults , r[i][1] , r[i][0] , gym , mini_bar , extra_bed ,checkin_date , checkout_date, dates_reserved_str ,  0  ))
                
        #Inserting dates into room table
                cursor.execute('''UPDATE Room_table SET reserved_dates = ? WHERE Room_no = ?''',  ( y, r[i][0] ))


                conn.commit()
                break

                

        
       
        
        else:
            print(i)
            i=i+1

advance_booking( name = "Rishit Aggarwal" , email = "2445@gmail.com" , adults = 3  , number = 647643 , room_type = "standard room", preference ="nil", gym="yes" , mini_bar="yes" , extra_bed ="yes" , checkin_date = "25-10-2023" , checkout_date = "28-10-2023")
        
        

