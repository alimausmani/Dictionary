# Q25. Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.
# Sample string : 'w3resource'
# Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}


b="w3resource"
c={}
for i in b:
    if i in c:
        c[i]+=1
    else:
        c[i]=1    
print("frequecy:\n"+str(c))        