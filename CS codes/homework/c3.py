
import random

def rando(a,b):
    c= random.randrange(a+1,b)
    return c

a=int(input("Enetr thr number "))
b=int(input("Enetr thr number "))

d=rando(a,b)
print(d)