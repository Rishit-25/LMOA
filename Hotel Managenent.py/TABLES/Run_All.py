import sqlite3



def Mother_table():
    conn = sqlite3.connect("HOTEL MANAGEMENT 1.db")
    cursor = conn.cursor()
        
    cursor.execute('''
                    CREATE TABLE Mother_table (
                        name  text,
                        booking_id integer PRIMARY KEY,
                        phone_no integer,
                        email_id text,
                        adults integer,
                        Room_no integer,
                        Room_type  text,
                        gym     text,
                        mini_bar    text,
                        extra_bed text,
                        check_in text,
                        check_out text,
                        reserved_dates text,  
                        Amount_payable integer      )
                ''')

Mother_table()
    





def Booking_table():
    conn = sqlite3.connect("HOTEL MANAGEMENT 1.db")
    cursor = conn.cursor()
        
    cursor.execute('''
                    CREATE TABLE Booking_table (
                        booking_id INTEGER PRIMARY KEY ,
                        Room_no  integer  ,
                        Room_type text,
                        name text,
                        email text,
                        number integer,
                        adults integer,
                        preference text ,
                        gym     text,
                        mini_bar    text,
                        extra_bed text,
                        reserved_dates text
                       
                         )
                ''')
 
Booking_table()












                                                      
def Room_table():
    conn = sqlite3.connect("HOTEL MANAGEMENT 1.db")
    cursor = conn.cursor()
        
    cursor.execute('''
                    CREATE TABLE Room_table (
                        Room_no  integer ,
                        Room_type text,
                        preference text,
                        reserved_dates text
                         )
                ''')

Room_table()   


conn = sqlite3.connect("HOTEL MANAGEMENT 1.db")
cursor = conn.cursor()   
insert_data = [
        101, "standard room"  ,  "nil" , "",
        102, "standard room"  ,  "nil" , "",
        103, "standard room"  ,  "nil" , "",
        104, "standard room"  ,  "nil" , "",
        106, "standard room"  , "nil" , "",
        107, "standard room"  , "nil" , "",
        108, "standard room"  , "nil","",
        109, "standard room"  , "nil","",
        110, "standard room"  , "nil","",
        111, "standard room"  , "nil","",
        112, "standard room"  , "nil","",
        113, "standard room"  , "nil","",
        114, "standard room"  , "nil","",
        115, "standard room"  , "nil","",
        116, "standard room"  , "nil","",
        117, "standard room"  , "nil","",
        118, "standard room"  , "nil","",
        119, "standard room"  , "nil","",
        120, "standard room"  , "Honeymoon","",
        121, "standard room"  , "Honeymoon","",
        122, "standard room"  , "Honeymoon","",
        123, "standard room"  , "Honeymoon","",
        124, "standard room"  , "Honeymoon","",
        125, "standard room"  , "Smoking rooms","",
        126, "standard room"  , "Smoking rooms","",
        127, "standard room"  , "Smoking rooms","",
        128, "standard room"  , "Smoking rooms","",
        129, "standard room"  , "Smoking rooms","",
        131, "standard room"  , "Smoking rooms","",
        133, "standard room"  , "Dedicated Workspaces","",
        132, "standard room"  , "Dedicated Workspaces","",
        134, "standard room"  , "Dedicated Workspaces","",
        135, "standard room"  , "Dedicated Workspaces","",
        136, "standard room"  , "Dedicated Workspaces","",
        137, "standard room"  , "Dedicated Workspaces","",
        138, "standard room"  , "Dedicated Workspaces","",
        139, "standard room"  , "Dedicated Workspaces","",
                


        201, "Deluxe room"  , "Honeymoon","",
        202, "Deluxe room"  , "Honeymoon","",
        203, "Deluxe room"  , "Honeymoon","",
        204, "Deluxe room"  , "Honeymoon","",
        206, "Deluxe room"  , "Dedicated Workspaces","",
        207, "Deluxe room"  , "Dedicated Workspaces","",
        208, "Deluxe room"  , "Dedicated Workspaces","",
        209, "Deluxe room"  , "Smoking rooms","",
        210, "Deluxe room"  ," Smoking rooms","",
        211, "Deluxe room"  ,"nil","",
        212, "Deluxe room"  ,"nil","",
        213, "Deluxe room"  ,"nil","",
        214, "Deluxe room"  ,"nil","",
        215, "Deluxe room"  ,"nil","",
        216, "Deluxe room"  ,"nil","",
        217, "Deluxe room"  ,"nil","",
        218, "Deluxe room"  ,"nil","",
        219, "Deluxe room"  ,"nil","",
        220, "Deluxe room"  ,"nil","",


        301, "Premier suite"  ,"nil","",
        302, "Premier suite"  ,"nil","",
        303, "Premier suite"  ,"nil","",
        304, "Premier suite"  ,"nil","",
        306, "Premier suite"  ,"nil","",
        307, "Premier suite"  ,"nil","",
        308, "Premier suite"  ,"Honeymoon","",
        309, "Premier suite"  ,"Honeymoon","",
        310, "Premier suite"  ,"Dedicated Workspaces","",
        311, "Premier suite"  ,"Dedicated Workspaces","",
        312, "Premier suite"  ,"Smoking rooms","",
        313, "Premier suite"  ,"Smoking rooms","",
        314, "Premier suite"  ,"Kanchenjunga view","",
        315, "Premier suite"  ,"Kanchenjunga view","",
        316, "Premier suite"  ,"Kanchenjunga view","",

        401, "Executive suite"  ,"nil","",
        402, "Executive suite"  ,"nil","",
        403, "Executive suite"  ,"nil","",
        404, "Executive suite"  ,"nil","",
        406, "Executive suite"  ,"nil","",
        407, "Executive suite"  ,"nil","",
        408, "Executive suite"  ,"nil","",
        409, "Executive suite"  ,"nil","",
        410, "Executive suite"  ,"nil","",
        411, "Executive suite"  ,"nil","",
        412, "Executive suite"  ,"Kanchenjunga view","",
        413, "Executive suite"  ,"Kanchenjunga view",""

        ]

for i in range (0,len(insert_data),4 ):
                                
    cursor.execute('''INSERT INTO Room_table (Room_no , Room_type,preference,reserved_dates) 
                    VALUES(?,?,?,?) ''',(insert_data[i],insert_data[i+1],insert_data[i+2],insert_data[i+3] )  ) 
    conn.commit()    

cursor.execute("SELECT * FROM Room_table")

r= cursor.fetchall()

print(r)

    

  