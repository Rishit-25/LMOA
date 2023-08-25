def copy(n):
    file1=open(n, "r+" )
    file2=open("copy.dat" , "w+")
    a=file1.readlines()
    print(max(a))
    for i in a:
        b="@" + i
        file2.write(b)

n=input("Enetr the name of the file : ")      
copy(n)