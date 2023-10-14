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
        
        n = len(past)  
        for k in range(n):
            for j in range(0, n - k - 1):
                if past[j] > past[j + 1]:
                    
                    past[j], past[j + 1] = past[j + 1], past[j]


        n = len(future)  
        for k in range(n):
            for j in range(0, n - k - 1):
                if future[j] < future[j + 1]:
                    
                    future[j], future[j + 1] = future[j + 1], future[j]
                

sorting_time()

print(past)

print("this is each element of past")
for i in past :
    print(i)
print("this is each element of future")
for i in future :
    print(i)
