import csv

file = open("student.csv" , "a+")
csv_writer = csv.writer(file)
csv_writer.writerow(["admission number", "name" , "class" ])
file.close()

def create() :
    global file
    file = open("student.csv" , "a+")
    a = input("Enter admiswsion number : ")
    b = input("Enter name : ")
    c = input("Enter marks : ")
    csv_writer = csv.writer(file)
    csv_writer.writerow([a,b,c])
    file.close()

def read() :
    global file
    file = open("student.csv" , "r")
    file_reader = csv.reader(file)
    for i in file_reader :
        print(i)
    file.close()

while True :
    print(''' Do you want to :
            1. Write data 
            2. Read data
            3. Exit
                ''')
    n=int(input("Enter the no. of what you want to do : "))
    if n==1:
        create()
    elif n== 2 :
        read()
    elif n == 3 :
        break







import csv
import os

if os.path.isfile(r"C:\Users\student\Desktop\student.csv"):
    pass
else:
    file = open(r"C:\Users\student\Desktop\student.csv" , "a+", newline = "")
    csv_writer = csv.writer(file)
    csv_writer.writerow(["admission number", "name" , "class" ])
    file.close()


def create() :
    global file
    file = open(r"C:\Users\student\Desktop\student.csv" , "a+" , newline = "")
    a = input("Enter admiswsion number : ")
    b = input("Enter name : ")
    c = input("Enter marks : ")
    csv_writer = csv.writer(file)
    csv_writer.writerow([a,b,c])
    file.close()

def read() :
    global file
    file = open(r"C:\Users\student\Desktop\student.csv", "r" , newline = "")
    file_reader = csv.reader(file)
    for i in file_reader :
        print(i)
    file.close()

while True :
    print(''' Do you want to :
            1. Write data 
            2. Read data
            3. Exit
                ''')
    n=int(input("Enter the no. of what you want to do : "))
    if n==1:
        create()
    elif n== 2 :
        read()
    elif n == 3 :
        break
