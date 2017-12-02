#!/root/anaconda3/bin/python

#A-1
def num_check (num, low, high):
    return (num >= low and num <=high)

print (num_check(4,2,10))

#A-2

#Write a Python function that accepts a string and calculate the number of upper case 
#letters and lower case letters.

st ='Hello Mr. Rogers, how are you this fine Tuesday?'
def count_char (st):
    cap = 0
    small = 0
    blanks = 0
    for c in st:
        if ('A' <= c and c <= 'Z'):
            cap+=1 
        elif ('a' <= c) and c <= 'z':
            small+=1
        else:
            blanks+=1

    print ("capitol letters : ", cap)
    print ("small leiptters : ", small)
    print ("Blanks : ", blanks)

count_char (st)

#A-3

l = [1,1,1,1,1,2,2,2,2,3,3,3,4,5,6]

def unique_elm (l):
    s = set(l)
    print(list(s))

unique_elm (l)

#A-4

num = [2,3,7,5,6]

def multiply_num (num):
    res = 1
    for i in num:
        res = res *i
    print (res)    

multiply_num(num)
