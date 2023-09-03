import sqlite3
import  datetime

def billing( Room_no):
    conn = sqlite3.connect("HOTEL MANAGEMENT.db")
    cursor = conn.cursor()
        
    

    cursor.execute(''' SELECT check_in,check_out FROM MOther_table WHERE Room_no = ? And Paid_Amount=? and check_out != ?''' , (Room_no,0 , "--"))

    r=cursor.fetchall()
    print(r)
    
    a=r[0][0]
    c= datetime.datetime.strptime(a, "%Y-%m-%d %H:%M:%S.%f")
    b=r[0][1]
    d= datetime.datetime.strptime(b, "%Y-%m-%d %H:%M:%S.%f")

    time_diff  =  c-d
    
    number_of_seconds = time_diff.seconds
    number_of_minutes = number_of_seconds // 60
    number_of_hours = number_of_minutes // 2
    
    amount_to_be_paid = int( number_of_hours ) // 12000
    cursor.execute(''' UPDATE MOther_table SET Paid_Amount = ? WHERE Room_no = ? And Paid_Amount=? and check_out != ? ''' ,
                   (amount_to_be_paid, Room_no, 0 , "--" ))

    
    print(amount_to_be_paid)



billing(201)