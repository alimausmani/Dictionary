# Write a Python script to add a key to a dictionary.
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}


dict={0:10,1:20}
for k in dict:
    pass
dict[k+1] = dict[k]+10
print(dict) 

# dict={0:10,1:20}
# dict[1+1]=dict[1]+10
# print(dict)

# dict={0:10,1:20}
# b={}
# for key in dict:
#     b[key+1]=dict[key]+10
# print(b)    

