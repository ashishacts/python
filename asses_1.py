#!/root/anaconda3/bin/python

#Assesment - 1

st = 'Print only the words that start with s in this sentence'
strlist=st.split(' ')
print (strlist)
for s in strlist:
    if(s[0] == 's'):
        print(s)

#Assesment - 2
# Use range() to print all the even numbers from 0 to 10

for i in range (11):
    if (i % 2 == 0):
        print (i)


#Assesment - 3
#Use List comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.

mylist = [elm for elm in range (1,50) if (elm % 3 == 0)]
print(mylist)


#Assesment - 4
#Go through the string below and if the length of a word is even print "even!"

evenstr = 'Print every word in this sentence that has an even number of letters'
evenlist = evenstr.split(' ')
for word in evenlist:
    if (len(word) % 2 == 0):
        print(word)


#Assesment - 5

#Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

for j in range(1,100):
    if (j % 3 == 0 and j % 5 == 0):
        print("FizzBuzz")
    elif(j % 3 == 0):
        print("Fizz")
    elif(j % 5 == 0):
        print("Buzz")
    else:
        print(j)



#Assesment - 6
#Use List Comprehension to create a list of the first letters of every word in the string below:

newst = 'Create a list of the first letters of every word in this string'
newltr = [elm[0] for elm  in newst.split(' ')]

print (newltr)

























