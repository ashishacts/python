#!/root/anaconda3/bin/python

s = "aabcbaa"
strln=len(s)
i = 0
j = strln-1
while (i < j):
    if (s[i] == s[j]):
        i+=1
        j-=1
    else:
        break
if (i >= j):
        print ("String is palindrom")
else:
        print ("String is NOT  palindrom")
