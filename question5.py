# Write a Python program to sort (ascending and descending) a dictionary by value.
# Original dictionary : {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# Dictionary in ascending order by value : [(0, 0), (2, 1), (1, 2), (4, 3), (3, 4)]
# Dictionary in descending order by value : {3: 4, 4: 3, 1: 2, 2: 1, 0: 0}


num=int(input("enter the number:"))
a={}
for i in range(1,num):
    a[i]=i**2
print(a)    


num=int(input("enter the number:"))
a={}
for i in range(1,num):
    a[i]=i**2
print(a)    


import operator
b={1:2,3:4,4:3,2:1,0:0}
asc=dict(sorted(b.items(),Key=operator.itemgetter(1)))
print("ascending = ",asc)

des=dict(sorted(b.items(),key=operator.itemgetter(1),reverse=True))
print("descending = ",des)


