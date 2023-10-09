import sqlite3
import datetime

past =[]
present=[]
future =[]
past_date = []
present_date=[]
future_date =[]

def sorting_time():

    conn = sqlite3.connect("HOTEL MANAGEMENT.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Mother_table")
    m = cursor.fetchall()

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
        
        for i in past :
            date_objects = datetime.datetime.strptime( i[10] , "%d-%m-%Y").date()
            print(date_objects)
            past_date.append(date_objects)
        
        for i in past :
            date_past = datetime.datetime.strptime( i , "%d-%m-%Y").date()
            print(date_past)
            if date_past == max(past_date):
                c = max(past_date)
                del(c)
                
            

sorting_time()


print(past)
print(present)
print(future)
