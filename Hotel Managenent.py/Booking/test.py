 
        for i in present :
            date_objects2 = datetime.datetime.strptime( i[10] , "%d-%m-%Y").date()
            print(date_objects2)
            present_date.append(date_objects2)
        
        for i in present :
            date_present = datetime.datetime.strptime( i , "%d-%m-%Y").date()
            print(date_past)
            if date_present == max(present_date):
                c = max(present_date)
                del(c)
        
        
        for i in future :
            date_objects3 = datetime.datetime.strptime( i[10] , "%d-%m-%Y").date()
            print(date_objects3)
            present_date.append(date_objects3)
        
        for i in future :
            date_future = datetime.datetime.strptime( i , "%d-%m-%Y").date()
            print(date_future)
            if date_future == max(future_date):
                c = max(future_date)
                del(c)