import pickle

def write_data(l) :
    file = open("performance.dat" , "wb+")
    pickle.dump(l , file)
    file.close()

list = []
while True:
    n = input("Enter name : ")
    m = input("Enter marks : ")
    l = [n,m]
    list.append(l)

l= [["ri" , 34],["rishit" , 40],["rishit" , 60],["rishit" , 67],["rist" , 33]]
write_data(l) 

file = open("performance.dat" , "rb+")
f=pickle.load(file)
print(f)
file.close()

def search_data() :
    file = open("performance.dat" , "rb+")
    f=pickle.load(file)
    print(f)
    for k in f:
        if k[1] >= 40:
            print(k)

search_data()




