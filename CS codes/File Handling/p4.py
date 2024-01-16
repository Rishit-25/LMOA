import os
file="marks.dat"
if os.path.isfile(file):
    data=open(file,"r+")
    print(len(data.readlines()))


