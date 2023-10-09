
import datetime


def discount(check_in):
    global amount_to_be_paid
    
    # Finding the month the month
    date = datetime.datetime.strptime(check_in, "%d-%m-%Y")   
    month = date.month
    print("Month:", month)

    if month == 5 or month == 6 or month == 7 :
        dis = 0.1 * amount_to_be_paid
        amount_to_be_paid = amount_to_be_paid - dis
    elif month == 1 or month == 12 or month == 11 :
        dis = 0.1 * amount_to_be_paid
        amount_to_be_paid = amount_to_be_paid - dis 

