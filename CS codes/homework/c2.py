def Addition(a,b):
    c=a+b
    print(c)  
def Substraction(a,b):
    d=a-b
    print(d)  
def multiplcation(a,b):
    e=a*b
    print(e) 
def division(a,b):
    if b==0 :
        print("divide by 0 error.Enetr again.")
    else :
        f=a/b
        print(f)
    

n=input("Enetr the operaton")
a=int(input("Enetr a number : "))

b=int(input("Enetr a number : "))

if n=="addition" :
    Addition(a,b)
elif n=="substrwtion" :
    Substraction(a,b)
elif n=="multipilcation" :
    multiplication(a,b)
elif n=="division" :
    division(a,b)
    