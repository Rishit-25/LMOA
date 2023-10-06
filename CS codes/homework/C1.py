def convert(a):
    b=int(a,8)
    c=hex(b)
    d=bin(b)
    print("octal to decimal value is :" , b)
    print("octal to hex value is  :" , c )
    print("octal to binary value is  :" , d )
octal=input("enter the octal value : ")   
convert(octal)

