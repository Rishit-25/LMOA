file1=open("Otherfile.dat" , "w+")
a=file1.readlines()
vowels = ["a" , "e" , "i" , "o" , "u" ]
for i in a:
    for j in i :
        for k in j:
            if k in vowels:
                if k.isupper() :
                    k=k.lower()
                elif k.islower():
                    k=k.upper()

print(a)