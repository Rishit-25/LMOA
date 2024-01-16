
# To push object who live in goa to stack
status = []
l= [ ["gurdas" , 4682346823 , "Goa"],
   ["rishit", 4682346823 , "Mumbai"],
   ["vaibhav", 4682346823 , "ranchi"],
   ["deep", 4682346823 , "Goa"]
       ]
top=-1

def push_element(l):
    global top
    i=0
    while i < len(l):
        
        if l[i][2] == "Goa" :
            b=[l[i][0] , l[i][1]]
            status.append(b)
            top= top+1
        i=i+1

def pop_element():
    global top 
    if top == -1:
        print("Stack Underflow")
    else:
        b=status.pop()
        print(b)
        top =top-1
push_element(l)
print("the stack is  :" , status)

pop_element()
print("the new stack is : " ,status)