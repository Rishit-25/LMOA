import sqlite3
import datetime


def discount(check_in, amount_payable ):
    
    # Finding the month the month
    date = datetime.datetime.strptime(check_in, "%d-%m-%Y")   
    month = date.month
    print("Month:", month)

    if month == 5 or month == 6 or month == 7 :
        dis = 0.1 * amount_payable
        amount_payable= amount_payable - dis
    elif month == 1 or month == 12 or month == 11 :
        dis = 0.1 * amount_payable
        amount_payable = amount_payable - dis 

    return amount_payable


def billing( booking_id ):
    conn = sqlite3.connect("HOTEL MANAGEMENT.db")
    cursor = conn.cursor()
   
    cursor.execute(''' SELECT * FROM MOther_table WHERE booking_id = ? ''' , ( booking_id ,)) 
    r=cursor.fetchall()
    print(r)

    check_in = r[0][10]
    room_type = r[0][6]
    gym =  r[0][7]
    mini_bar =  r[0][8]
    extra_bed =  r[0][9]
    reserved_dates = r[0][12]
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
        
        service_tax = 0.12 * amount_to_be_paid
        vat = 0.14 * amount_to_be_paid
        room_service_tax = 0.05 * amount_to_be_paid

        amount_to_be_paid = amount_to_be_paid + service_tax + vat + room_service_tax 

        #checking the discount
        dis_amount = discount(check_in, amount_to_be_paid)
        amount_to_be_paid = dis_amount
        
    
    
    if room_type == "Premier suite":
        amount_to_be_paid = 10000*count

        if gym =="yes" :
            amount_to_be_paid = amount_to_be_paid + (500*count)
        elif mini_bar =="yes" :
            amount_to_be_paid = amount_to_be_paid + (500*count)
        elif extra_bed =="yes" :
            amount_to_be_paid = amount_to_be_paid + (500*count)

        service_tax = 0.12 * amount_to_be_paid
        vat = 0.14 * amount_to_be_paid
        room_service_tax = 0.05 * amount_to_be_paid

        amount_to_be_paid = amount_to_be_paid + service_tax + vat + room_service_tax 

        #checking the discount
        dis_amount = discount(check_in, amount_to_be_paid)
        amount_to_be_paid = dis_amount

    if room_type == "Executive suite":
        amount_to_be_paid = 12000*count

        if gym =="yes" :
            amount_to_be_paid = amount_to_be_paid + (500*count)
        elif mini_bar =="yes" :
            amount_to_be_paid = amount_to_be_paid + (500*count)
        elif extra_bed =="yes" :
            amount_to_be_paid = amount_to_be_paid + (500*count)

        service_tax = 0.12 * amount_to_be_paid
        vat = 0.14 * amount_to_be_paid
        room_service_tax = 0.05 * amount_to_be_paid

        amount_to_be_paid = amount_to_be_paid + service_tax + vat + room_service_tax 

        #checking the discount
        dis_amount = discount(check_in, amount_to_be_paid)
        amount_to_be_paid = dis_amount


    if room_type == "standard room":
        amount_to_be_paid = 6000*count

        if gym =="yes" :
            amount_to_be_paid = amount_to_be_paid + (500*count)
        elif mini_bar =="yes" :
            amount_to_be_paid = amount_to_be_paid + (500*count)
        elif extra_bed =="yes" :
            amount_to_be_paid = amount_to_be_paid + (500*count)

        service_tax = 0.12 * amount_to_be_paid
        vat = 0.14 * amount_to_be_paid
        room_service_tax = 0.05 * amount_to_be_paid

        amount_to_be_paid = amount_to_be_paid + service_tax + vat + room_service_tax 

        # checking the discount 
        dis_amount = discount(check_in, amount_to_be_paid)
        amount_to_be_paid = dis_amount
    
    cursor.execute(''' UPDATE MOther_table SET Amount_payable = ? WHERE booking_id = ? ''' ,
                (amount_to_be_paid, booking_id))
    conn.commit()

    
    print(amount_to_be_paid)
    
    


billing(4)
