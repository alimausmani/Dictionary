# Q4. Write a Python script to print a dictionary where the keys are numbers between 1 and
# 15 (both included) and the values are square of keys.
# Simple Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12:
# 144, 13: 169, 14: 196, 15: 225}.


# num=int(input("enter the number"))
# a={}
# for i in range(1,num):
#     a[i]=i**2
# print(a)


# a={} 
# for i in range(1,16):
#     a[i]=i**2
# print(a)


list1=[1,2,3,4,5,6]
d1=dict(enumerate(list1))
print(d1)

# list1=[1,2,3,4,5,6]
# b={}
# i=0
# for j in range(len(list1)):
#     b[i]=list1[j]
#     i+=1
# print(b)    

# Q54.
# Write a Python program to create a key-value list pairings in a given dictionary.
# Original dictionary:
# {1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['Zachary
# Simon']}
# A key-value list pairings of the said dictionary:
# [{1: 'Jean Castro', 2: 'Lula Powell', 3: 'Brian Howell', 4: 'Lynne Foster', 5: 'Zachary Simon'}]
 

# a={1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['Zachary Simon']}
# res=[]
# for i,j in a.items():
#   for k in j:
#     d={i:k}
#     res.append(d)
# print(res)