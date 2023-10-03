import sqlite3
import datetime

past =[]
present=[]
future =[]

def sorting_time():

    conn = sqlite3.connect("HOTEL MANAGEMENT.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Mother_table")
    m = cursor.fetchall()

    current_date = datetime.datetime.now().date()
    print(current_date)
    
    i=0
    
    while i <=(len(m)-1):
        d = m[i][9] 
        print(d)
        
        date = datetime.datetime.strptime(d , "%d-%m-%Y").date()
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
            
        date_objects = datetime.datetime.strptime(date, "%d-%m-%Y").date()

sorting_time()


print(past)
print(present)
print(future)
