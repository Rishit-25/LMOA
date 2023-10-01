x = c[0][0]

                    for h in dates_reserved:
                        y = x + " , " + h
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
        
        

