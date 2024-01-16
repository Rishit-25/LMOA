file1 = open("marks.dat", "r+")

a = file1.readlines()
print("The data in the file before - ",a)

x=0
for i in range(len(a)):
    for k in a[i]:
        x=x+1
print("The size of the file is  : " , x )