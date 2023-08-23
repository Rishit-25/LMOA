myfile = open("Otherfile.dat", "r+")
content = myfile.readlines()
for line in myfile:
    print(line)