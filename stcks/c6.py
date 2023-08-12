rr= [2,3,4,45,6,7]

def pop(rr):
    if len(rr) == 0 :
        print("stk underflow")
    else:
        e=len(rr) -1
        while e>= 0 :
            print(rr[e])
            e=e-1

pop(rr)