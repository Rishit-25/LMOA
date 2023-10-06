import sqlite3


def billing( Room_no,name):
    conn = sqlite3.connect("HOTEL MANAGEMENT.db")
    cursor = conn.cursor()
   



    
    
    cursor.execute(''' SELECT * FROM MOther_table WHERE Room_no = ? And name = ? ''' , (Room_no, name )) 
    r=cursor.fetchall()
    print(r)


    room_type = r[0][5]
    gym =  r[0][6]
    mini_bar =  r[0][7]
    extra_bed =  r[0][8]
    reserved_dates = r[0][11]
    print(reserved_dates)
    
    
    count = reserved_dates.count(",")
    print(count)


    if room_type == "Deluxe room":
        amount_to_be_paid = 8000*count

        if gym =="yes" :
            amount_to_be_paid = amount_to_be_paid + (500*count)
        elif mini_bar =="yes" :
            amount_to_be_paid = amount_to_be_paid + (500*count)
        elif extra_bed =="yes" :
            amount_to_be_paid = amount_to_be_paid + (500*count)
        
        
    
    
    if room_type == "Premier suite":
        amount_to_be_paid = 10000*count

        if gym =="yes" :
            amount_to_be_paid = amount_to_be_paid + (500*count)
        elif mini_bar =="yes" :
            amount_to_be_paid = amount_to_be_paid + (500*count)
        elif extra_bed =="yes" :
            amount_to_be_paid = amount_to_be_paid + (500*count)


    if room_type == "Executive suite":
        amount_to_be_paid = 12000*count

        if gym =="yes" :
            amount_to_be_paid = amount_to_be_paid + (500*count)
        elif mini_bar =="yes" :
            amount_to_be_paid = amount_to_be_paid + (500*count)
        elif extra_bed =="yes" :
            amount_to_be_paid = amount_to_be_paid + (500*count)



    if room_type == "standard room":
        amount_to_be_paid = 6000*count

        if gym =="yes" :
            amount_to_be_paid = amount_to_be_paid + (500*count)
        elif mini_bar =="yes" :
            amount_to_be_paid = amount_to_be_paid + (500*count)
        elif extra_bed =="yes" :
            amount_to_be_paid = amount_to_be_paid + (500*count)
    
    cursor.execute(''' UPDATE MOther_table SET Amount_payable = ? WHERE Room_no = ? and name = ? ''' ,
                (amount_to_be_paid, Room_no,  name))
    conn.commit()

    
    print(amount_to_be_paid)
    
    


billing(125,"Rishit Aggarwal")
