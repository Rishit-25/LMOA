def change(l):
    for i in range(0,len(l)-1,2):
        l[i],l[i+1]=l[i+1],l[i]

    print(l)
    

l= input("")
l=list(l)
change(l)

