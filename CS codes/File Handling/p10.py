file1 = open("marks.dat", "r+")

a = file1.readlines()
print("The data in the file before - ",a)

vowels = ["a", "e", "i", "o", "u"]

# Manipulate the vowels in the lines
for i in range(len(a)):
    for k in a[i]:
        if k.lower() in vowels:
            if k.isupper():
                a[i] = a[i].replace(k, k.lower())
            elif k.islower():
                a[i] = a[i].replace(k, k.upper())

file1.seek(0)
file1.writelines(a)
file1.seek(0)
a = file1.readlines()
print("The data in the file After - ",a)

file1.close()