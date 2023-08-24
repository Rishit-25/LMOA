def longest_line(n):
    file1=open(n, "r+" )
    a=file1.readlines()
    print(max(a))
    for i in file1.readlines():
        
        if i ==max(file1.readlines()):
            print("this the files longest line : " , max(file1.readlines()))

n= input("enetr the name of the fiel : ")
longest_line(n)