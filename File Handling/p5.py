n=input("Enter the file name with extention  : " )
n2 = input("Enter the second file name with extention  : " )

file1 = open(n , r+)
file2 = open(n2 ,  w+)
a=file1.readlines()

for i in a:
    if i[0].islower():
        file2.write(i)
