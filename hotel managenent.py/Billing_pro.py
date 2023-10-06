import sqlite3
import  datetime

def billing( Room_no,name):
    conn = sqlite3.connect("HOTEL MANAGEMENT.db")
    cursor = conn.cursor()
   



    
    try:
        cursor.execute(''' SELECT * FROM MOther_table WHERE Room_no = ? And name = ? ''' , (Room_no, name )) 
        r=cursor.fetchall()
        print(r)


        room_type = r[0][5]
        gym =  r[0][6]
        mini_bar =  r[0][7]
        extra_bed =  r[0][8]

       
        
        
    

    
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



billing(125)






start_date = datetime.datetime.strptime(start_date_str, '%Y-%m-%d')
end_date = datetime.datetime.strptime(end_date_str, '%Y-%m-%d')
    
current_date = start_date
    
while current_date <= end_date:
    print(current_date.strftime('%Y-%m-%d'))
    current_date += datetime.timedelta(days=1)