import pickle

count= 0 
def write_data() :
    global count
    file = open("performance.dat" , "ab")

    n = input("Enter name : ")
    m = int(input("Enter marks : "))
    l = [n,m]
    print("This is l : " , l)
    pickle.dump(l , file)
    file.close()
    count= count + 1
    
def search_data() :
    a=[]
    file = open("performance.dat" , "rb")
    for i in range(count):
        f=pickle.load(file)
        print("This is f : " ,f)
        a.append(f)
    for k in a:
        if k[1] >= 40:
            print(k)

while True :
    print(''' Do you want to :
            1. Write data 
            2. Search data
            3. Exit
                ''')
    n=int(input("Enter the no. of what you want to do : "))
    if n==1:
        write_data()
    elif n== 2 :
        search_data()
    elif n == 3 :
        break



import pickle

count= 0 
def write_data() :
    global count
    file = open(r"C:\Users\student\Desktop\performance.dat" , "ab")

    n = input("Enter name : ")
    m = int(input("Enter marks : "))
    l = [n,m]
    print("This is l : " , l)
    pickle.dump(l , file)
    file.close()
    count= count + 1
    
def search_data() :
    a=[]
    file = open(r"C:\Users\student\Desktop\performance.dat" , "rb")
    for i in range(count):
        f=pickle.load(file)
        
        a.append(f)
    for k in a:
        if k[1] >= 40:
            print(k)

while True :
    print(''' Do you want to :
            1. Write data 
            2. Search data
            3. Exit
                ''')
    n=int(input("Enter the no. of what you want to do : "))
    if n==1:
        write_data()
    elif n== 2 :
        search_data()
    elif n == 3 :
        break
    
    

    








