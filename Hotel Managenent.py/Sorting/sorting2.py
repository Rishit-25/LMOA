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

    conn = sqlite3.connect("HOTEL MANAGEMENT 1.db")
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
            date_objects1 = datetime.datetime.strptime( k[10] , "%d-%m-%Y").date()
            print(date_objects1)
            past_date.append(date_objects1)
        
        for f in past_date :
           
            if f == max(past_date):
               
                for j in past:
                    date_obj = datetime.datetime.strptime( j[10] , "%d-%m-%Y").date()
                    if date_obj == f :     
                        past1.append(j)
                        c = max(past_date)
                        print("this is the max past date :" ,  c)
                        past_date.remove(c)
                        
        

                
            

sorting_time()

print("this is past " , past)
for p in past :
    print(p)
z=0
print( "this is past 1 lists " , past1 )
print( "this is each element past 1 lists "  )

for i in past1:
    print(i)
    z=z+1
print(z)
print(present)
print(future)
