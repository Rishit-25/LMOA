import sqlite3
import  datetime

def billing( Room_no):
    conn = sqlite3.connect("HOTEL MANAGEMENT.db")
    cursor = conn.cursor()
    
    try:
        cursor.execute(''' SELECT check_in,check_out FROM MOther_table WHERE Room_no = ? And Paid_Amount=? and check_out != ?''' , (Room_no,0 , "--"))
    

        r=cursor.fetchall()
        
        cursor.execute(''' SELECT Room_type FROM MOther_table WHERE Room_no = ? And Paid_Amount=? and check_out != ?''' , (Room_no,0 , "--"))
        r2=cursor.fetchall()
        
        room_type = r2[0][0]
    

    
        a=r[0][0]
        c= datetime.datetime.strptime(a, "%Y-%m-%d %H:%M:%S.%f")
        b=r[0][1]
        d= datetime.datetime.strptime(b, "%Y-%m-%d %H:%M:%S.%f")

        time_diff  =  d-c
        print(time_diff)
        
        number_of_seconds = time_diff.seconds
        print(number_of_seconds)
        number_of_minutes = number_of_seconds // 60
        print(number_of_minutes)
        number_of_hours = number_of_minutes // 2
        print(number_of_hours)
        if room_type == "Deluxe room":
            amount_to_be_paid = int( number_of_hours ) // 1
        elif room_type == "Premier suite":
            amount_to_be_paid = int( number_of_hours ) // 2
        if room_type == "Executive suite":
            amount_to_be_paid = int( number_of_hours ) // 3
        if room_type == "standard room":
            amount_to_be_paid = int( number_of_hours ) // 4
        
        cursor.execute(''' UPDATE MOther_table SET Paid_Amount = ? WHERE Room_no = ? and check_out != ? ''' ,
                    (amount_to_be_paid, Room_no,  "--" ))
        conn.commit()

        
        print(amount_to_be_paid)
    
    except:
        print("YOU NEED TO CHECK OUT FIRST!!!!!!!!!!!!!!!!!")



billing(101)