d={ "pencil": 20 , "notebook" : 300 , "eraser" : 76 }
top = -1
stck=[]
def push(d):
    global top
    for key in d:
        if d[key]> 75 :
            stck.append(key)
            top=top+1

push(d)
print("The stack is " , stck)