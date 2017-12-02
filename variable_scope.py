#!/root/anaconda3/bin/python

x = 50

def myint ():
    x = 20
    print ("After local variable assignement: ", x)

print ("Before local variable of x : ", x)
myint()


def newglobal ():
    global x
    x = 50000
    print ("After local variable assignement: ", x)
    def oldglobal():
        x = 50
        print ("old global x = ", x)
    oldglobal ()

newglobal ()
print ("After global variable changed x : ", x)
