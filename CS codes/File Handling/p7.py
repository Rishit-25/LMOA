def find_numbers(n):
    l=[]
    file1=open(n, "r+" )
    file1.seek(0)
    a=file1.readlines()
    
    for i in range(len(a)):
        for j in a[i]:
            if j.isnumeric():
                l.append(j)
    print("This the data of the file : " , a )
    print("These are the numbers in this file : " , l) 
n= input("enetr the name of the file : ")
print
find_numbers(n)