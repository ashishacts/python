#!/root/anaconda3/bin/python

mystring="My Mom world!!"
strln=len(mystring)

for i in range(strln):
    if (mystring[i] == 'M'):
        print("i = ", i, mystring[i:])
        yourstring = 'N' + mystring[i+1:]
        print("yourstring = ", yourstring)

