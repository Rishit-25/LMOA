def copy(n):
    file1=open(n, "r+" )
    file2=open("Otherfile.dat" , "w+")
    a=file1.readlines()
    for i in a:
        if i[0] != "@":
            file2.write(i)

n=input("Enter the name of the file : ")      
copy(n)