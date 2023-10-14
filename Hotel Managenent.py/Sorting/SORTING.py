import sqlite3
import datetime

past =[]
present=[]
future =[]
past1 =[]
present1=[]
future1 =[]
past_date = []
present_date=[]
future_date =[]

def sorting_time():

    conn = sqlite3.connect("HOTEL MANAGEMENT.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Mother_table")
    m = cursor.fetchall()
    print(m)

    current_date = datetime.datetime.now().date()
    print(current_date)
    
    i=0
    
    while i <=(len(m)-1):
        d = m[i][10] 
        print(d)
        
        date = datetime.datetime.strptime( d , "%d-%m-%Y").date()
        print(date)
             
        if date <  current_date:
            past.append(m[i])
            i=i+1
        elif date == current_date:
            present.append(m[i])
            i=i+1
        else:
            future.append(m[i])
            i=i+1
        
        for k in past :
            print("this is date in past list " , k[10])
            print(type(k[10]))
            date_objects1 = datetime.datetime.strptime( k[10] , "%d-%m-%Y").date()
            print(date_objects1)
            past_date.append(date_objects1)
        
        for k in past_date :
            print(type(k))
            print("this past date" , k)
            date_past = k
            print(date_past)
            if date_past == max(past_date):
                c = max(past_date)
                for j in past:
                    date_obj = datetime.datetime.strptime( j[10] , "%d-%m-%Y").date()
                    if date_obj == date_past :     
                        past1.append(j)
                del(c)

sorting_time()

print(past1)
