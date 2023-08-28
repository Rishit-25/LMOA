myfile = open("Otherfile.dat", "r+")
content = myfile.readlines()
i=0
for line in content:
    for j in line:
        if j != " " and j!="\n" :
            i= i +1

print(i)