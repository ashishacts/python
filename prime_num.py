#!/root/anaconda3/bin/python
import math

x = input('Enter Fist number : ')
xint = int (x)


def is_prime (xint):
    if (xint == 1 or xint == 2):
        print (xint, "is a Prime Number")
        return
    if (xint % 2  == 0):
        print (xint, "is NOT a Prime Number")
        return

    for i in range (3, int(math.sqrt(xint))):
        if (xint % i == 0):
            break 

    if (i + 1 == xint):
        print (xint, "is a Prime Number")
    else:
        print (xint, "is NOT a Prime Number")



is_prime (xint)




