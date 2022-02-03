# Q18.Write a Python program to get the maximum and minimum value in a dictionary.


# k=int(input("enter the number:"))
# b={}
# for i in range(0,k,1):
#     k=int(input("enter the key:"))
#     v=int(input("enter the value:"))
#     b.update({k:v})
# print(b)     
# max = 0
# for  i in b :
#     if b[i]>max:
#         max=b[i]
# print(max,"it is a maximum number")        
   


# k=int(input("enter the number:"))
# b={}
# for i in range(0,k,1):
#     k=int(input("enter the key:"))
#     v=int(input("enter the value:"))
#     b.update({k:v})
# print(b)   



num=int(input("enter the number:"))
b={}
for i in range(num):
    k=input("enter the key:")
    if num[i]==str(1):
       print("one",end=" ")
    elif num[i]==str(2):
        print("two",end=" ")
    elif num[i]==str(3):
        print("three",end=" ")           
    elif num[i]==str(4):
        print("four",end=" ")           
    elif num[i]==str(5):
        print("five",end=" ")  
    b.update({k:i})
print(b)    
