# Debug Code

# Now we will debug the code related to dictionary.

# question:-1

# You have been given a dictionary in which you have 
# to print the value of some key. Debug the code.

# details={
#     "name":"shanti",
#     "age":12,
#     "email":"shanti@navgurukul.org",
# }

# print(details["name"])
# print(details["email"])
# print(details["age"])




# question:-2

# You have been given a dictionary in which you have to find the sum of 
# all the keys. You have to debug this code and find out how you can get the output as 14.

# dict1={1:2,2:3,3:4,4:5}
# sum=0
# for i in dict1.values():
#     sum+=i
# print(sum)    

# question:-3

# Below is a program in which the keys are between 1 
# to 15 and the values ​​are the squares of the keys.

# The output should be something like this:-
# <br>{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64,<br>9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

# Now, you have to debug this :-

# c={}
# for i in range(1,16):
#     c[i]=i**2
# print(c) 
# 
#    
# question:-4

# You have been given two dictionaries, You need to concatenate them.

# Now you have to debug the code
# And your output should be like this :-

# {'umesh':21,'bijender':54,'amar':67,'peter':89,'sonu':56,'python':20,"gaurav":300,'dev':34,"karan":43}

# s={'umesh':21,'bijender':54,'amar':67,'peter':89,'sonu':56,'python':20,"gaurav":300,'dev':34,"karan":43}
# a={'python':20,"gaurav":300,'dev':34,"karan":43}
# c={}
# for i in (s,a):
#     c.update(i)
# print(c)    