def find_numbers(n):
    l=[]
    file1=open(n, "r+" )
    file1.seek(0)
    a=file1.readlines()
    print(a)
    for i in a:
        for j in i:
            if j.isnumeric():
                l.append(j)
    print(l) 
n= input("enetr the name of the fiel : ")
find_numbers(n)