#!/root/anaconda3/bin/python

mylist = [(10,20), (28,0), (12,-1), (43, 38)]
mykeys = {'k1':1, 'k2':2, 'k3':3}

for elm in mylist:
    print (elm)

for (t1,t2) in mylist:
    print (t1)


for (k,v) in mykeys.items():
    print (k,v)

print ("While Loop Example : ")

a = 1
while a < 10:
    print("a = ", a)
    a+=1
    if (a==3):
        break
    else:
        print("Continuing")
else:
    print("All Done")

xlist = range(10,20,2)
for i in xlist:
    print(i)

print ("List comprehension: ")

ylist = [x for x in range(2,30)]
ylist.append(1000)
for i in ylist:
    print (i)
